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
        self.match_results = MatchResults()
        self.tournament_manager = TournamentManager(
            self.TOURNAMENT_FILE,
            self.tournaments_data,
            self.data_display,
            self.data_manager,
        )
        self.player_manager = PlayerManager(
            self.PLAYER_FILE, self.players_data, self.data_display, self.data_manager
        )

    def handle_tournaments_menu(self, user_choice):
        match user_choice:
            case "1":
                return self.tournament_manager.list_tournament()
            case "2":
                return self.tournament_manager.create_tournament()
            case "3":
                return self.tournament_manager.manage_tournament(
                    self.menu,
                    self.handle_tournament_management,
                )
            case "4":
                return None

    def handle_players_menu(self, user_choice):
        match user_choice:
            case "1":
                return self.player_manager.list_player_by_id()
            case "2":
                return self.player_manager.list_player_by_last_name()
            case "3":
                return self.player_manager.create_player()
            case "4":
                return None

    def handle_tournament_management(self, user_choice, id):
        selected_tournament = next(t for t in self.tournaments_data if t["id"] == id)

        match user_choice:
            case "1":
                # Ajouter des joueurs au tournoi
                print(self.player_manager.list_player_by_id())
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
                    if not any(
                        existing_player["id"] == player["id"]
                        for existing_player in selected_tournament["players"]
                    ):
                        selected_tournament["players"].append(player)
                        player["score"] = 0
                        print(
                            f"{player['first_name']} {player['last_name']} a été ajouté au tournoi."
                        )
                    else:
                        print("Ce joueur fait déjà partie du tournoi.")

                self.data_manager.save_data(self.TOURNAMENT_FILE, self.tournaments_data)
                return "Ajout de joueurs terminé."

            case "2":
                try:
                    players_data = selected_tournament["players"]
                    return self.data_display.format_tournament_players(players_data)
                except KeyError:
                    return "Aucun joueur dans ce tournoi."

            case "3":
                # Générer les matchs
                try:
                    players = selected_tournament["players"]
                except KeyError:
                    return "Aucun joueur dans ce tournoi."

                turn_number = int(selected_tournament["turn"])
                for i in range(1, turn_number + 1):
                    current_turn = Turn(f"Round {i}")
                    print(f"\nRound {i} - Match:")

                    if i == 1:
                        matches = self.tournament_manager.shuffle(current_turn, players)
                    else:
                        matches = self.tournament_manager.sort_by_score(
                            current_turn, players
                        )
                    print(matches)
                    self.match_results.display_turn_matches(matches)
                    current_turn.end_turn()

                    self.tournament_manager.update_player_score(
                        selected_tournament, players
                    )
                    self.data_manager.save_data(
                        self.TOURNAMENT_FILE, self.tournaments_data
                    )

                return "Match terminés."

            case "4":
                return "Match affichés."

            case "5":
                return None
