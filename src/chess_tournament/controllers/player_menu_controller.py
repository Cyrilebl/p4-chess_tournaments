from src.chess_tournament.models import Player, DataManager
from src.chess_tournament.views import PlayerView, InformativeMessage, DisplayData
from .player_controller import PlayerController


class PlayerMenuController:
    def __init__(self):
        self.player_controller = PlayerController(
            Player, DataManager(), DisplayData(), PlayerView(), InformativeMessage()
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
