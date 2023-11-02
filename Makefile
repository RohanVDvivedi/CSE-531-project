compile_protobuf: branch.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./branch.proto

run: python3 ./main.py

check:
	python3 ./checker_part_1.py ./customer_output.json
	python3 ./checker_part_2.py ./branch_output.json
	python3 ./checker_part_3.py ./events_output.json