from grpc_out import hello_pb2_grpc, hello_pb2
import grpc
from concurrent import futures

class HelloWorldService(hello_pb2_grpc.HelloWorldServicer):
    def __init__(self):
        pass

    def hello(self, request, context):
        print("Recieved request from client with request: ", request)

        return hello_pb2.HelloResponse(name=f"Hi, {request.name}")
    
    def age(self, request, context):
        print("Recieved request from client with request: ", request)
        return hello_pb2.AgeResponse(answer=f"Age is {request.age}")

if __name__ == "__main__":
    print("gRPC server running on 9009")
    server = grpc.server(futures.ThreadPoolExecutor())
    hello_pb2_grpc.add_HelloWorldServicer_to_server(HelloWorldService(), server)
    server.add_insecure_port("[::]:9009")
    server.start()
    server.wait_for_termination()