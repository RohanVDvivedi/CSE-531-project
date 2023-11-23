compile_protobuf: branch.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./branch.proto

run:
	python3 ./main.py

check:
	python3 checker.py ./customer_events.json