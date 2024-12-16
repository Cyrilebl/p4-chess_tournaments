from .display import display_players, display_tournaments
from src.chess_tournament.models import Player, Tournament
from src.chess_tournament.controllers import MenuManager
from . import Menu

class MenuHandler:
  FOLDER_PATH = "src/data"
  TOURNAMENT_FILE = "tournaments.json"
  PLAYER_FILE = "players.json"
  
  def handle_tournaments_menu(self, user_choice):
    menu_manager = MenuManager()
    
    match user_choice :
      case "1":
        # Afficher la liste des tournois
        tournaments_data = menu_manager.load_data(self.FOLDER_PATH, self.TOURNAMENT_FILE)
        
        if tournaments_data is None:
          return "Aucun tournoi enregistré."
        else:
          return display_tournaments(tournaments_data)
      
      case "2":
        # Créer un tournoi
        tournaments_data = menu_manager.load_data(self.FOLDER_PATH, self.TOURNAMENT_FILE)
        existing_ids = [tournament["id"] for tournament in tournaments_data]
        id = max(existing_ids, default=0) + 1
        
        name = input("Nom: ")
        place = input("Lieu: ")
        start_date = input("Date de début (JJ/MM/AAAA): ")
        end_date = input("Date de fin (JJ/MM/AAAA): ")
        description = input("Description: ").capitalize() or "Pas de description"
        turn = input("Nombre de tours (4 par défaut): ") or 4
        
        tournament = Tournament(id, name, place, start_date, end_date, turn, description)
        tournaments_data = [tournament.add_tournament()]
        menu_manager.save_to_json(self.FOLDER_PATH, self.TOURNAMENT_FILE, tournaments_data)
        
        return "Le tournoi a été ajouté avec succès."
      
      case "3":
        return None

  
  def handle_players_menu(self, user_choice):
    menu_manager = MenuManager()
    
    match user_choice :     
      case "1":
        # Afficher la liste des joueurs
        players_data = menu_manager.load_data(self.FOLDER_PATH, self.PLAYER_FILE)
        
        if players_data is None:
          return "Aucun joueur enregistré."
        else:
          return display_players(players_data)
        
      case "2":        
        # Ajouter un joueur
        players_data = menu_manager.load_data(self.FOLDER_PATH, self.PLAYER_FILE)
        existing_ids = [player["id"] for player in players_data]
        id = max(existing_ids, default=0) + 1
        
        first_name = input("Prénom du joueur: ")
        last_name = input("Nom de famille: ")
        birth_date = input("Date de naissance (JJ/MM/AAAA): ")
        
        player = Player(id, first_name, last_name, birth_date)
        players_data = [player.add_player()]

        menu_manager.save_to_json(self.FOLDER_PATH, self.PLAYER_FILE, players_data)
        
        return "Le joueur a été ajouté avec succès."
        
      case "3":
        return None
  