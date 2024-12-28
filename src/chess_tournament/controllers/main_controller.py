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

    def handle_submenu(self, menu_view, controller, exit_choice):
        while True:
            sub_choice = menu_view()
            if sub_choice == exit_choice:
                break
            controller(sub_choice)

    def run(self):
        while True:
            user_choice = self.menu.main_menu()
            match user_choice:
                case 1:
                    self.handle_submenu(
                        self.menu.players_menu,
                        self.player_menu_controller.handle_players_menu,
                        4,
                    )

                case 2:
                    self.handle_submenu(
                        self.menu.tournaments_menu,
                        self.tournament_menu_controller.handle_tournaments_menu,
                        3,
                    )

                case 3:
                    self.tournament_setup_menu_controller.tournament_choice()
                    self.handle_submenu(
                        self.menu.tournament_setup_menu,
                        self.tournament_setup_menu_controller.handle_tournament_setup_menu,
                        6,
                    )

                case 4:
                    self.informative_message.quit_program()
                    return
