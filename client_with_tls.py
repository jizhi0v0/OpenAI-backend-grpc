import grpc
import openai_pb2 as oai_pb2
import openai_pb2_grpc as oai_pb2_grpc
import time

def run():
    # 创建 gRPC 通道
    with open('your pem file path!', 'rb') as f:
        certificate_chain = f.read()
        channel = grpc.secure_channel('domain:tls port', grpc.ssl_channel_credentials(root_certificates=certificate_chain))
        # 创建客户端存根
        stub = oai_pb2_grpc.OpenAIStub(channel)

        while True:
            # 构造请求消息
            request = oai_pb2.ChatRequest()
            request.apikey = "your apikey"
            request.question = "Hello World!"

            # 发送请求并获取响应
            response = stub.chat(request)
            # 处理响应
            if response.success:
                print("Response message:", response.message)
            else:
                print("Error:", response.message)


if __name__ == '__main__':
    run()
