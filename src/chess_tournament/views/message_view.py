class MessageView:
    def quit_program(self):
        print("\nÀ bientôt !")

    def return_to_menu(self):
        input("\nAppuyez sur Entrée pour revenir au menu...")

    def new_entity_success(self, entity_name):
        print(f"\nLe {entity_name} a été ajouté avec succès.")

    def invalid_id(self):
        print("Veuillez entrer un ID valide.")

    def player_already_registered(self):
        print("Ce joueur fait déjà partie du tournoi.")

    def ask_tournament_id(self):
        return input("\nEntrez l'ID du tournoi à gérer: ")

    def ask_player_id(self):
        return input("\nEntrez l'ID du joueur à ajouter (ou 'q' pour quitter): ")

    def generate_new_matches(self):
        print(
            "\nScores du round en cours déjà inscrits. Veuillez générer de nouveaux match."
        )

    def record_scores(self):
        print("\nVeuillez inscrire les scores des matchs du round en cours.")

    def can_t_generate_more_matches(self):
        print("Les matchs de tous les tours ont déjà été générés.")

    def display_error(self, error_message):
        print(f"Une erreur s'est produite: {error_message}")
