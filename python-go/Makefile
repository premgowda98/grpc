generate_grpc_python:
	@python3 -m grpc_tools.protoc -Iprotos --python_out=./python-server/grpc_out --grpc_python_out=./python-server/grpc_out protos/hello.proto

generate_grpc_go:
	@protoc -Iprotos --go_out=./go-client/grpc_out --go-grpc_out=./go-client/grpc_out protos/hello.proto