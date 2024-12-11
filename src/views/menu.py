from .player_view import display_players
from .player_view import load_data

class Menu:
  
  def choice(self):
    print("""
-----------------------------
      TOURNOIS D'ECHECS
-----------------------------
  
=== MENU ===

[1] Créer un nouveau tournoi
[2] Tournois existants
[3] Joueurs
[4] Créer un nouveau joueur
[5] Modifier un joueur
""")
  
    choice = input("Entrez votre choix: ")
  
    while choice not in ["1", "2", "3", "4"]:
      choice = input("Choix invalide. Entrez votre choix: ")
    
    return choice

  def display(self, choice):
    match choice :
        case "1":
          result = ""
        case "2":
          result = ""
        case "3":
          file_path = "src/data/players.json"
          players_data = load_data(file_path)
          result = display_players(players_data)
        case "4":
          result = ""
        case "5":
          result = ""  
        case _:
          print("Choix invalide.")
                 
    return result