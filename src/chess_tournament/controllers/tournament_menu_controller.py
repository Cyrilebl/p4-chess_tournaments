from src.chess_tournament.models import Tournament, DataManager
from src.chess_tournament.views import TournamentView, MessageView, Formatter
from .tournament_controller import TournamentController


class TournamentMenuController:
    def __init__(self):
        self.tournament_controller = TournamentController(
            Tournament,
            DataManager(),
            Formatter(),
            TournamentView(),
            MessageView(),
        )

    def handle_tournaments_menu(self, user_choice):
        match user_choice:
            case 1:
                return self.tournament_controller.list_tournament()
            case 2:
                return self.tournament_controller.add_tournament()
            case 3:
                return
