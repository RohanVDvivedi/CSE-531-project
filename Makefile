compile_protobuf: branch.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./branch.proto

run:
	python3 ./main.py ./input_big.json

check:
	python3 checker.py ./events_output.json