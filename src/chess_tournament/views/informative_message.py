class InformativeMessage:
    def quit_program(self):
        print("\nÀ bientôt !")

    def new_entity_success(self, entity_name):
        print(f"\nLe {entity_name} a été ajouté avec succès.")

    def return_to_menu(self):
        input("\nAppuyez sur Entrée pour revenir au menu...")

    def invalid_id(self):
        print("Veuillez entrer un ID valide.")

    def player_already_registered(self):
        print("Ce joueur fait déjà partie du tournoi.")

    def ask_tournament_id(self):
        return input("\nEntrez l'ID du tournoi à gérer: ")

    def ask_player_id(self):
        return input("\nEntrez l'ID du joueur à ajouter (ou 'q' pour quitter): ")
