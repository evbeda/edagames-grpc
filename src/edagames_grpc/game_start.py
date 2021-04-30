from typing import Dict

from edagames_grpc import eda_games_pb2
from edagames_grpc.utils import struct_to_dict


class GameStart:
    game_id: str
    current_player: str
    turn_data: Dict

    def __init__(
        self,
        game_id: str,
        current_player: str,
        turn_data: Dict,
    ):
        self.game_id = game_id
        self.current_player = current_player
        self.turn_data = turn_data

    def to_protobuf_struct(self) -> eda_games_pb2.GameStartResponse:
        response = eda_games_pb2.GameStartResponse()
        response.idgame = self.game_id
        response.current_player = self.current_player
        response.turn_data.update(self.turn_data)
        return response

    @staticmethod
    def from_protobuf_game_start_response(
        game_start_response: eda_games_pb2.GameStartResponse,
    ) -> 'GameStart':
        return GameStart(
            game_start_response.idgame,
            game_start_response.current_player,
            struct_to_dict(game_start_response.turn_data),
        )
