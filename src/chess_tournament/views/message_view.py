class MessageView:
    def quit_program(self):
        print("\nÀ bientôt !")

    def return_to_menu(self):
        input("\nAppuyez sur Entrée pour revenir au menu...")

    def new_entity_success(self, entity_name):
        print(f"\nLe {entity_name} a été ajouté avec succès.")

    def player_already_registered(self):
        print("\nCe joueur fait déjà partie du tournoi.")

    def ask_tournament_id(self):
        return input("\nEntrez l'ID du tournoi à gérer: ")

    def ask_player_id(self):
        return input("\nEntrez l'ID du joueur à ajouter (ou 'q' pour quitter): ")

    def scores_already_updated(self):
        print("\nLes scores pour ce round ont déjà été mis à jour.")

    def record_scores(self):
        print("\nVeuillez inscrire les scores pour le round en cours.")

    def can_t_generate_more_matches(self):
        print("Les matchs de tous les tours ont déjà été générés.")

    def no_player(self):
        print("\nAucun joueur enregistré.")
