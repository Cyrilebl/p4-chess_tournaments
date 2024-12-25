from src.chess_tournament.models import Tournament, DataManager
from src.chess_tournament.views import TournamentView, InformativeMessage, DisplayData
from .tournament_setup_controller import TournamentSetupController
from .tournament_menu_controller import TournamentMenuController


class TournamentSetupMenuController:
    def __init__(self):
        self.tounament_setup_controller = TournamentSetupController(
            Tournament,
            DataManager(),
            DisplayData(),
            TournamentView(),
            InformativeMessage(),
        )
        self.selected_tournament = None

    def tournament_choice(self):
        self.selected_tournament = self.tounament_setup_controller.tournament_choice()
        return self.selected_tournament

    def handle_tournament_setup_menu(self, user_choice):
        match user_choice:
            case 1:
                return self.tounament_setup_controller.add_player(
                    self.selected_tournament
                )
            case 2:
                return self.tounament_setup_controller.list_tournament_players(
                    self.selected_tournament
                )
            case 3:
                return ""
            case 4:
                return self.tounament_setup_controller.list_matches(
                    self.selected_tournament
                )
            case 5:
                return None
