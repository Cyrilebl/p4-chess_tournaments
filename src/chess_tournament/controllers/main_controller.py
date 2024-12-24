from src.chess_tournament.views import Menu, InformativeMessage
from .player_menu_controller import PlayerMenuController
from .tournament_menu_controller import TournamentMenuController


class MainController:
    def __init__(self):
        self.menu = Menu()
        self.informative_message = InformativeMessage()
        self.player_menu_controller = PlayerMenuController()
        self.tournament_menu_controller = TournamentMenuController()

    def run(self):
        while True:
            user_choice = self.menu.main_menu()
            match user_choice:
                case 1:
                    sub_choice = self.menu.players_menu()
                    self.player_menu_controller.handle_players_menu(sub_choice)
                case 2:
                    sub_choice = self.menu.tournaments_menu()
                    self.tournament_menu_controller.handle_tournaments_menu(sub_choice)
                case 3:
                    self.menu.handle_tournament_menu()
                case 4:
                    self.informative_message.quit_program()
                    exit()
