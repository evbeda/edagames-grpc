from typing import Dict
from google.protobuf.struct_pb2 import Struct


def struct_to_dict(data: Struct) -> Dict:
    converted = {}
    for k, v in data.items():
        if isinstance(v, Struct):
            v = struct_to_dict(v)
        converted[k] = v
    return converted
