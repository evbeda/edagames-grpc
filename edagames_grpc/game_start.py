from typing import Dict

import eda_games_pb2


class GameStart:
    id_game: str
    next_player: str
    turn_data: Dict

    def __init__(
        self,
        id_game: str,
        next_player: str,
        turn_data: Dict,
    ):
        self.id_game = id_game
        self.next_player = next_player
        self.turn_data = turn_data

    def to_protobuf_struct(self) -> eda_games_pb2.GameStartResponse:
        response = eda_games_pb2.GameStartResponse()
        response.id_game = self.id_game
        response.next_player = self.next_player
        response.turn_data.update(self.turn_data)
        return response

    @staticmethod
    def from_protobuf_game_start_response(
        game_start_response: eda_games_pb2.GameStartResponse,
    ) -> 'GameStart':
        return GameStart(
            game_start_response.id_game,
            game_start_response.next_player,
            game_start_response.turn_data,
        )
