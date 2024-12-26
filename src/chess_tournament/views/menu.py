class Menu:
    def user_choice_error(self, number_of_choices):
        while True:
            try:
                user_choice = int(input("Entrez votre choix: "))
                if 0 < user_choice <= number_of_choices:
                    return user_choice
                else:
                    print("Choix invalide... ")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro.")

    def main_menu(self):
        print(
            """
---------------------------------
        TOURNOIS D'ECHECS
---------------------------------

=== MENU PRINCIPAL ===

[1] Gestion des joueurs
[2] Gestion des tournois
[3] Configurer un tournoi
[4] Quitter
"""
        )

        return self.user_choice_error(4)

    def tournaments_menu(self):
        print(
            """
=== TOURNOIS ===

[1] Liste des tournois
[2] Créer un nouveau tournoi
[3] Menu principal
"""
        )

        return self.user_choice_error(3)

    def players_menu(self):
        print(
            """
=== JOUEURS ===

[1] Liste des joueurs (ID)
[2] Liste des joueurs (Ordre alphabétique)
[3] Ajouter un nouveau joueur
[4] Menu principal
"""
        )

        return self.user_choice_error(4)

    def tournament_setup_menu(self):
        print(
            """
=== CONFIGURATION ===

[1] Ajouter des joueurs
[2] Voir les joueurs
[3] Générer les matchs
[4] Voir les matchs
[5] Entrer les scores
[6] Retour
"""
        )

        return self.user_choice_error(6)
