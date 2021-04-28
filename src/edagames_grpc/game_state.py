from typing import Dict

from edagames_grpc import eda_games_pb2


class GameState:
    previous_player: str
    current_player: str
    turn_data: Dict
    play_data: Dict

    def __init__(
        self,
        previous_player: str,
        current_player: str,
        turn_data: Dict,
        play_data: Dict,
    ):
        self.previous_player = previous_player
        self.current_player = current_player
        self.turn_data = turn_data
        self.play_data = play_data

    def to_protobuf_struct(self) -> eda_games_pb2.GameStateResponse:
        response = eda_games_pb2.GameStateResponse()
        response.previous_player = self.previous_player
        response.current_player = self.current_player
        response.turn_data.update(self.turn_data)
        response.play_data.update(self.play_data)
        return response

    @staticmethod
    def from_protobuf_game_state_response(
        game_state_response: eda_games_pb2.GameStateResponse,
    ) -> 'GameState':
        return GameState(
            game_state_response.previous_player,
            game_state_response.current_player,
            game_state_response.turn_data,
            game_state_response.play_data
        )
