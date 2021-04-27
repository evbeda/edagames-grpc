# edagames-grp

gRPC interface for edagames platform-game communication

## Compiling

To compile protobuf definition into Python files install grpcio-tools and execute

`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./eda_games.proto`

## Examples

Examples for simple client and server are located in the [examples folder](examples)

To run them each example use:
- Client: `python -m examples.client`
- Server: `python -m examples.server`
