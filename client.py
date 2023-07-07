import grpc

import openai_pb2 as oai_pb2
import openai_pb2_grpc as oai_pb2_grpc


def run():
    # 创建 gRPC 通道
    with grpc.insecure_channel('localhost:40055') as channel:
        # 创建客户端存根
        stub = oai_pb2_grpc.OpenAIStub(channel)

        while True:
            # 构造请求消息
            request = oai_pb2.ChatRequest()
            request.apikey = "your apikey"
            request.question = "Hello World!"
            # 设置其他请求参数...

            # 发送请求并获取响应
            response = stub.chat(request)
            # 处理响应
            if response.success:
                print("Response message:", response.message)
            else:
                print("Error:", response.message)


if __name__ == '__main__':
    run()
