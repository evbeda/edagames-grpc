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


## Package

- Command to install the package:

'pip install edagames-grpc'

- Steps for running a new version package with changes:

1) Change the version in the setup.py
2) run: 'python setup.py bdist_wheel sdist' to update the package locally
3) run: 'twine upload dist/*' to upload the new package version to pypi