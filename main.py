from src.chess_tournament.views import Menu
from src.chess_tournament.controllers import MenuHandler


def main():
    menu = Menu()
    menu_handler = MenuHandler()

    user_choice = menu.main_menu()

    if user_choice == "1":
        while True:
            sub_choice = menu.tournaments_menu()
            result = menu_handler.handle_tournaments_menu(sub_choice)
            if result is None:
                main()
            elif result:
                print(f"\n{result}")

            input("\nAppuyez sur Entrée pour revenir au menu des tournois...")

    elif user_choice == "2":
        while True:
            sub_choice = menu.players_menu()
            result = menu_handler.handle_players_menu(sub_choice)
            if result is None:
                main()
            elif result:
                print(f"\n{result}")

            input("\nAppuyez sur Entrée pour revenir au menu des joueurs...")

    elif user_choice == "3":
        print("\nAu revoir !")
        exit()


if __name__ == "__main__":
    main()
