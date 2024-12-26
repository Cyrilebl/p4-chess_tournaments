from src.chess_tournament.views import Menu, MessageView
from .player_menu_controller import PlayerMenuController
from .tournament_menu_controller import TournamentMenuController
from .tournament_setup_menu_controller import TournamentSetupMenuController


class MainController:
    def __init__(self):
        self.menu = Menu()
        self.informative_message = MessageView()
        self.player_menu_controller = PlayerMenuController()
        self.tournament_menu_controller = TournamentMenuController()
        self.tournament_setup_menu_controller = TournamentSetupMenuController()

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
                    self.tournament_setup_menu_controller.tournament_choice()
                    sub_choice = self.menu.tournament_setup_menu()
                    self.tournament_setup_menu_controller.handle_tournament_setup_menu(
                        sub_choice
                    )
                case 4:
                    self.informative_message.quit_program()
                    exit()
