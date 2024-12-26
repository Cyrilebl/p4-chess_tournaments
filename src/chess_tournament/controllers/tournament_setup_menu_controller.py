from src.chess_tournament.models import (
    Tournament,
    Turn,
    DataManager,
    TurnManager,
)
from src.chess_tournament.views import (
    TournamentView,
    InformativeMessage,
    DisplayData,
    Matches,
)
from .tournament_setup_controller import TournamentSetupController


class TournamentSetupMenuController:
    def __init__(self):
        self.tounament_setup_controller = TournamentSetupController(
            Tournament,
            Turn,
            DataManager(),
            TurnManager(),
            DisplayData(),
            TournamentView(),
            InformativeMessage(),
            Matches(),
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
                return self.tounament_setup_controller.generate_matches(
                    self.selected_tournament
                )
            case 4:
                return self.tounament_setup_controller.list_matches(
                    self.selected_tournament
                )
            case 5:
                return self.tounament_setup_controller.register_score(
                    self.selected_tournament
                )
            case 6:
                return None