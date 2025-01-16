## Server

1. Use htis command to generate proto files `python3 -m grpc_tools.protoc -Iprotos --python_out=./grpc_out --grpc_python_out=./grpc_out protos/hello.proto`
2. This generates 2 files *_pb2_grpc.py and *_p2.py
3. Stub class is used by client to invoke the rpc
4. Servicer class deines interface to implement the service defined in the .proto file