from typing import Dict

import eda_games_pb2


class GameState:
    current_player: str
    next_player: str
    turn_data: Dict
    play_data: Dict

    def __init__(
        self,
        current_player: str,
        next_player: str,
        turn_data: Dict,
        play_data: Dict,
    ):
        self.current_player = current_player
        self.next_player = next_player
        self.turn_data = turn_data
        self.play_data = play_data

    def to_protobuf_struct(self) -> eda_games_pb2.GameStateResponse:
        response = eda_games_pb2.GameStateResponse()
        response.current_player = self.current_player
        response.next_player = self.next_player
        response.turn_data.update(self.turn_data)
        response.play_data.update(self.play_data)
        return response
