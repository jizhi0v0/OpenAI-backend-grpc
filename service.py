import time
import grpc
import openai
import requests
import json
import result_pb2 as rpb
import openai_pb2 as oai_pb2
import openai_pb2_grpc as oai_pb2_grpc
from concurrent import futures
from datetime import datetime
from requests.adapters import HTTPAdapter

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class OpenAIServicer(oai_pb2_grpc.OpenAIServicer):

    def __init__(self):
        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10)  # 根据需求设置连接池大小
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

    def get_models(self, request, context):
        apikey = request.apikey

        url = "https://api.openai.com/v1/models"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(apikey)
        }
        response = self.session.get(url, headers=headers)
        models_dicts = json.loads(response.content)

        result_util = rpb.Response()
        if 'error' in models_dicts:
            return rpb.Response(success=False,message=models_dicts['error']['message'])
        else:
            model_response_list = oai_pb2.ModelResponseList()
            for model_dict in models_dicts['data']:
                model_response = oai_pb2.ModelResponse()
                model_response.id = model_dict['id']
                model_response.created = model_dict['created']
                model_response_list.models.append(model_response)
            result_util.success = True
            result_util.data.Pack(model_response_list)

        return result_util
    
    def chat(self, request, context):
        apikey = request.apikey;
        question = request.question;
        default_model = 'gpt-3.5-turbo';
        model = request.model if request.model is not None and request.model != '' else default_model;

        openai.api_key = apikey
        messages = [{"role": "user", "content": question}]
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=0.7
            )
        except openai.error.AuthenticationError as e:
            return rpb.Response(success=False,message=str(e))

        return rpb.Response(success=True,message=response['choices'][0]['message']['content'])


# 创建 gRPC 服务器
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# 将服务类添加到服务器中
oai_pb2_grpc.add_OpenAIServicer_to_server(OpenAIServicer(), server)

# 定义服务器启动的地址和端口
server_address = '[::]:40055'

# 启动服务器
server.add_insecure_port(server_address)
server.start()

# 保持服务器运行，直到手动停止
try:
    while True:
        time.sleep(_ONE_DAY_IN_SECONDS)
except KeyboardInterrupt:
    server.stop(0)
