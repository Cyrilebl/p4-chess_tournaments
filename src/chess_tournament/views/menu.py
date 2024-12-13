class Menu:
  def handle_user_choice_error(self, array):
    user_choice = input("Entrez votre choix : ")
  
    while user_choice not in array:
      user_choice = input("Choix invalide. Entrez votre choix : ")

    return user_choice
   
  def main_menu(self):
    print("""
-----------------------------
      TOURNOIS D'ECHECS
-----------------------------
  
=== MENU PRINCIPAL ===

[1] Gestion des tournois
[2] Gestion des joueurs
[3] Quitter
""")
    
    return self.handle_user_choice_error(["1", "2", "3"])

  def tournaments_menu(self):
    print("""
=== TOURNOIS ===

[1] Liste des tournois
[2] Créer un nouveau tournoi
[3] Menu principal
""")
    
    return self.handle_user_choice_error(["1", "2", "3"])

  def players_menu(self):
    print("""
=== JOUEURS ===

[1] Liste des joueurs
[2] Ajouter un nouveau joueur
[3] Menu principal
""")
    
    return self.handle_user_choice_error(["1", "2", "3"])

  def turns_menu(self):
    print("""    
[1] Choisir un tournoi
[2] Ajouter un nouveau joueur
[3] Generer des match
[4] Voir les matchs
[5] Quitter
""")
    
    return self.handle_user_choice_error(["1", "2", "3", "4", "5"])
