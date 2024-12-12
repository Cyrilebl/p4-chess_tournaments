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
""")
  
    choice = input("Entrez votre choix: ")
  
    while choice not in ["1", "2", "3", "4"]:
      choice = input("Choix invalide. Entrez votre choix: ")
    
    return choice

  def display(self, choice):
    folder_path = "src/data"
    file_name = "players.json"
    
    match choice :
        case "1":
          result = ""
          
        case "2":
          result = ""
          
        case "3":
          players_data = load_data(folder_path, file_name)
          result = display_players(players_data)
          
        case "4":
          first_name = input("Prénom du joueur: ")
          last_name = input("Nom de famille: ")
          birth_date = input("Date de naissance (JJ/MM/AAAA): ")
          
          new_player = Player(first_name, last_name, birth_date)
          players_data = [new_player.add_player()]

          save_to_json(folder_path, file_name, players_data)
          
          result = "Le joueur a été ajouté avec succès."
          
        case "5":
          result = ""
          
        case _:
          result = print("Choix invalide.")
      
    return print(result)
  
  #si players.json existe pas, message d'erreur