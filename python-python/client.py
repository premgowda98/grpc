from grpc_out import hello_pb2_grpc, hello_pb2
import grpc

class HelloClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:9009")
        self.stub = hello_pb2_grpc.HelloWorldStub(self.channel)

    def hello(self, name):
        request = hello_pb2.HelloRequest(name=name)
        return self.stub.hello(request)
    
    def age(self, age):
        request = hello_pb2.AgeRequest(age=age)
        return self.stub.age(request)


if __name__=="__main__":
    client = HelloClient()
    response = client.hello(name="Guru")
    print(response)
    response2 = client.age(age=26)
    print(response2)