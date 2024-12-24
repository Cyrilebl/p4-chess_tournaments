class InformativeMessage:
    def quit_program(self):
        print("\nÀ bientôt !")

    def new_player_success(self):
        print("Le joueur a été ajouté avec succès.")

    def no_current_data(self, data):
        if data is None:
            print("Aucun joueur enregistré.")

    def return_to_menu(self):
        input("\nAppuyez sur Entrée pour revenir au menu...")
