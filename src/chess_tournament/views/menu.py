from .display import display_players, display_tournaments
from src.chess_tournament.models import Player, Tournament
from src.chess_tournament.controllers import MenuManager

class Menu:  
  def choice(self):
    print("""
-----------------------------
      TOURNOIS D'ECHECS
-----------------------------
  
=== MENU ===

[1] Liste des tournois
[2] Créer un nouveau tournoi
[3] Liste des joueurs
[4] Ajouter un nouveau joueur
[5] Modifier un joueur
[6] Quitter
""")
  
    choice = input("Entrez votre choix (1-6): ")
  
    while choice not in ["1", "2", "3", "4", "5", "6"]:
      choice = input("Choix invalide. Entrez votre choix (1-6): ")

    return choice

  def display(self, choice):
    menu_manager = MenuManager()
    FOLDER_PATH = "src/data"
    PLAYER_FILE = "players.json"
    TOURNAMENT_FILE = "tournament.json"
    
    match choice :
        case "1":
          # Afficher la liste des tournois
          tournaments_data = menu_manager.load_data(FOLDER_PATH, TOURNAMENT_FILE)
          
          if tournaments_data is None:
            result = "Aucun tournoi enregistré."
          else:
            result = display_tournaments(tournaments_data)
          
        case "2":
          # Créer un tournoi
          name = input("Nom: ")
          place = input("Lieu: ")
          start_date = input("Date de début (JJ/MM/AAAA): ")
          end_date = input("Date de fin (JJ/MM/AAAA): ")
          description = input("Description: ")
          description = description.capitalize() if description else "Pas de description"
          turn = input("Nombre de tours (4 par défaut): ")
          turn = turn if turn else 4
          
          tournament = Tournament(name, place, start_date, end_date, turn, description)
          tournament_data = [tournament.add_tournament()]

          menu_manager.save_to_json(FOLDER_PATH, TOURNAMENT_FILE, tournament_data)
          
          result = "Le tournoi a été ajouté avec succès."
          
        case "3":
          # Afficher la liste des joueurs
          players_data = menu_manager.load_data(FOLDER_PATH, PLAYER_FILE)
          
          if players_data is None:
            result = "Aucun joueur enregistré."
          else:
            result = display_players(players_data)
          
        case "4":
          # Ajouter un joueur
          first_name = input("Prénom du joueur: ")
          last_name = input("Nom de famille: ")
          birth_date = input("Date de naissance (JJ/MM/AAAA): ")
          
          player = Player(first_name, last_name, birth_date)
          players_data = [player.add_player()]

          menu_manager.save_to_json(FOLDER_PATH, PLAYER_FILE, players_data)
          
          result = "Le joueur a été ajouté avec succès."
          
        case "5":
          result = ""
        
        case "6":
          result = "Au revoir !"
          
        case _:
          result = print("Choix invalide.")
          
    return print(f"\n{result}")
  