from .display import display_players, display_tournaments
from src.chess_tournament.models import Player, Tournament
from src.chess_tournament.controllers import MenuManager
from . import Menu

class MenuHandler:
  FOLDER_PATH = "src/data"
  TOURNAMENT_FILE = "tournaments.json"
  PLAYER_FILE = "players.json"
  
  def handle_tournaments_menu(self, user_choice):
    menu = Menu()
    menu_manager = MenuManager()
    
    match user_choice :
      case "1":
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
      
      case "2":
        # Gestion d'un tournoi
        
        # Afficher la liste des tournois
        tournaments_data = menu_manager.load_data(self.FOLDER_PATH, self.TOURNAMENT_FILE)

        if tournaments_data is None:
          return "Aucun tournoi enregistré."
        else:
          print(display_tournaments(tournaments_data))
        
        choice = int(input("\nEntrez l'ID du tournoi à gérer: "))
        
        for tournament in tournaments_data:
          if tournament["id"] == choice:
            name = tournament["name"]
            place = tournament["place"]
            start_date = tournament["start_date"]
            end_date = tournament["end_date"]
            turn = tournament["turn"]
            print(f"Vous avez choisi le tournoi {name} à {place}\nDate: du {start_date} au {end_date}\nNombre de tours: {turn}")
        "Aucun tournoi ne correspond à cet ID."
        
        sub_choice = menu.tournament_management()
        
        return self.handle_tournament_management(sub_choice, choice)
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
  
  def handle_tournament_management(self, user_choice, id):
    menu_manager = MenuManager()
    tournaments_data = menu_manager.load_data(self.FOLDER_PATH, self.TOURNAMENT_FILE)
    
    selected_tournament = next(t for t in tournaments_data if t["id"] == id)
  
    match user_choice:
      case "1":
        # Voir les joueurs du tournoi
        try:
          players = selected_tournament["players"]
          return display_players(players)
        except:
            return "Aucun joueur dans ce tournoi."
      
      case "2":
        # Ajouter des joueurs au tournoi
        
        # Afficher la liste des joueurs
        players_data = menu_manager.load_data(self.FOLDER_PATH, self.PLAYER_FILE)
        
        if players_data is None:
          return "Aucun joueur enregistré."
        
        print(display_players(players_data))
        
        # Sélectionner un joueur
        new_player_id = input("Entrez l'ID du joueur à ajouter: ")
        
        # Trouver le joueur correspondant
        player = next((p for p in players_data if p["id"] == int(new_player_id)), None)
        if not player:
            return "Joueur introuvable."
        
        # Ajouter le joueur au tournoi
        if "players" not in selected_tournament:
          selected_tournament["players"] = []
        
        # Empêcher les doublons
        if player not in selected_tournament["players"]:
          selected_tournament["players"].append(player)
        else:
          return "Ce joueur fait déjà partie du tournoi."
        
        menu_manager.save_to_json(self.FOLDER_PATH, self.TOURNAMENT_FILE, tournaments_data)

        return f"{player['first_name']} {player['last_name']} a été ajouté au tournoi."
      
      case "3":
        # Générer les matchs pour le tour actuel
        return "Matchs générés pour le tour actuel."
      
      case "4":
        # Voir les matchs du tour actuel
        return "Matchs du tour actuel affichés."
      
      case "5":
        return None
