from src.chess_tournament.models import Player
from src.chess_tournament.views import PlayerView, InformativeMessage, DisplayData
from .data_controller import DataController
from .player_controller import PlayerController


class PlayerMenuController:
    def __init__(self):
        self.player_controller = PlayerController(
            Player, DisplayData(), PlayerView(), InformativeMessage(), DataController()
        )

    def handle_players_menu(self, user_choice):
        match user_choice:
            case 1:
                return self.player_controller.list_player_by_id()
            case 2:
                return self.player_controller.list_player_by_last_name()
            case 3:
                return self.player_controller.add_player()
            case 4:
                return None
