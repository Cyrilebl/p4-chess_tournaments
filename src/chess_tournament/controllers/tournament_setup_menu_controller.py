from src.chess_tournament.models import (
    Tournament,
    Turn,
    DataManager,
)
from src.chess_tournament.views import (
    Formatter,
    MessageView,
    TournamentView,
    MatchesView,
    Helpers,
)
from .tournament_setup_controller import TournamentSetupController
from .match_maker import MatchMaker


class TournamentSetupMenuController:
    def __init__(self):
        self.tounament_setup_controller = TournamentSetupController(
            Tournament,
            Turn,
            DataManager(),
            Formatter(),
            MessageView(),
            TournamentView(),
            MatchesView(),
            Helpers(),
            MatchMaker(),
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
                return self.tounament_setup_controller.ranking(self.selected_tournament)
            case 7:
                return
