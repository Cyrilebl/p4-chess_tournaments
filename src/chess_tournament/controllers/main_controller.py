from src.chess_tournament.views import Menu, InformativeMessage
from .player_menu_controller import PlayerMenuController


class MainController:
    def __init__(self):
        self.menu = Menu()
        self.informative_message = InformativeMessage()
        self.player_menu_controller = PlayerMenuController()

    def run(self):
        while True:
            user_choice = self.menu.main_menu()
            match user_choice:
                case 1:
                    sub_choice = self.menu.players_menu()
                    self.player_menu_controller.handle_players_menu(sub_choice)
                case 2:
                    self.menu.tournaments_menu()
                case 3:
                    self.menu.handle_tournament_menu()
                case 4:
                    self.informative_message.quit_program()
                    exit()
