# edagames-grp

To compile protobuf definition into Python files install grpcio-tools and execute

`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./eda_games.proto`
