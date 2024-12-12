from .player_view import display_players
from .player_view import load_data
from src.models import Player
from src.controllers import save_to_json

class Menu:
  
  def choice(self):
    print("""
-----------------------------
      TOURNOIS D'ECHECS
-----------------------------
  
=== MENU ===

[1] Créer un nouveau tournoi
[2] Tournois existants
[3] Liste des joueurs
[4] Créer un nouveau joueur
[5] Modifier un joueur
[6] Quitter
""")
  
    choice = input("Entrez votre choix: ")
  
    while choice not in ["1", "2", "3", "4", "5", "6"]:
      choice = input("Choix invalide. Entrez votre choix (1-6): ")
    
    return choice

  def display(self, choice):
    FOLDER_PATH = "src/data"
    FILE_NAME = "players.json"
    
    match choice :
        case "1":
          result = ""
          
        case "2":
          result = ""
          
        case "3":
          players_data = load_data(FOLDER_PATH, FILE_NAME)
          
          if players_data is None:
            result = "Aucun joueurs enregistrés."
          else:
            result = display_players(players_data)
          
        case "4":
          first_name = input("Prénom du joueur: ")
          last_name = input("Nom de famille: ")
          birth_date = input("Date de naissance (JJ/MM/AAAA): ")
          
          new_player = Player(first_name, last_name, birth_date)
          players_data = [new_player.add_player()]

          save_to_json(FOLDER_PATH, FILE_NAME, players_data)
          
          result = "Le joueur a été ajouté avec succès."
          
        case "5":
          result = ""
        
        case "6":
          result = "Au revoir !"
          
        case _:
          result = print("Choix invalide.")
      
    return print(result)
  