from src.chess_tournament.models import Turn
from src.chess_tournament.views import Menu, DataDisplay, MatchResults
from .data_manager import DataManager
from .tournament_manager import TournamentManager
from .player_manager import PlayerManager


class MenuManager:
    FOLDER_PATH = "src/data"
    TOURNAMENT_FILE = "tournaments.json"
    PLAYER_FILE = "players.json"

    def __init__(self):
        self.menu = Menu()
        self.data_manager = DataManager(self.FOLDER_PATH)
        self.players_data = self.data_manager.load_data(self.PLAYER_FILE)
        self.tournaments_data = self.data_manager.load_data(self.TOURNAMENT_FILE)
        self.data_display = DataDisplay(self.players_data, self.tournaments_data)
        self.tournament_manager = TournamentManager()
        self.player_manager = PlayerManager()
        self.match_results = MatchResults()

    def handle_tournaments_menu(self, user_choice):
        match user_choice:
            case "1":
                return self.tournament_manager.list_tournament(
                    self.tournaments_data, self.data_display
                )
            case "2":
                return self.tournament_manager.create_tournament(
                    self.TOURNAMENT_FILE, self.tournaments_data, self.data_manager
                )
            case "3":
                return self.tournament_manager.manage_tournament(
                    self.tournaments_data,
                    self.data_display,
                    self.menu,
                    self.handle_tournament_management,
                )
            case "4":
                return None

    def handle_players_menu(self, user_choice):
        match user_choice:
            case "1":
                return self.player_manager.list_player(
                    self.players_data, self.data_display
                )
            case "2":
                return self.player_manager.create_player(
                    self.PLAYER_FILE, self.players_data, self.data_manager
                )
            case "3":
                return None

    def handle_tournament_management(self, user_choice, id):
        selected_tournament = next(t for t in self.tournaments_data if t["id"] == id)

        match user_choice:
            case "1":
                # Ajouter des joueurs au tournoi
                if self.players_data is None:
                    return "Aucun joueur enregistré."
                print(self.data_display.format_players(self.players_data))

                while True:
                    # Sélectionner un joueur
                    new_player_id = input(
                        "Entrez l'ID du joueur à ajouter (ou 'q' pour quitter): "
                    )

                    if new_player_id.lower() == "q":
                        break

                    try:
                        # Trouver le joueur correspondant
                        player = next(
                            (
                                p
                                for p in self.players_data
                                if p["id"] == int(new_player_id)
                            ),
                            None,
                        )
                    except ValueError:
                        print("Veuillez entrer un ID valide.")
                        continue

                    if not player:
                        print("Joueur introuvable. Veuillez réessayer.")
                        continue

                    # Ajouter le joueur au tournoi
                    if "players" not in selected_tournament:
                        selected_tournament["players"] = []

                    # Empêcher les doublons
                    if player not in selected_tournament["players"]:
                        selected_tournament["players"].append(player)
                        print(
                            f"{player['first_name']} {player['last_name']} a été ajouté au tournoi."
                        )
                    else:
                        print("Ce joueur fait déjà partie du tournoi.")

                self.menu_manager.save_data(self.TOURNAMENT_FILE, self.tournaments_data)
                return "Ajout de joueurs terminé."

            case "2":
                # Voir les joueurs du tournoi
                try:
                    players = selected_tournament["players"]
                    return self.data_display.format_players(players)
                except KeyError:
                    return "Aucun joueur dans ce tournoi."

            case "3":
                # Générer les matchs
                try:
                    players = selected_tournament["players"]
                except KeyError:
                    return "Aucun joueur dans ce tournoi."

                for player in players:
                    player.pop("id")
                    player.pop("birth_date")
                    player["score"] = 0

                turn_number = int(selected_tournament["turn"])
                for i in range(1, turn_number + 1):
                    current_turn = Turn(f"Round {i}")
                    print(f"\nRound {i} - Match:")
                    if current_turn.name == "Round 1":
                        turn = self.tournament_manager.create_turn(
                            current_turn, players
                        )
                        print(turn)
                        self.match_results.display_turn_matches(turn)
                        current_turn.end_turn()
                    else:
                        turn = self.tournament_manager.create_turn(
                            current_turn, players
                        )
                        print(turn)
                        self.match_results.display_turn_matches(turn)

            case "4":
                # Voir les matchs
                return "Matchs affichés."

            case "5":
                return None
