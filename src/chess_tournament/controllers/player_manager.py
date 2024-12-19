from src.chess_tournament.models import Player, Tournament, Turn
from src.chess_tournament.views import Menu, DataDisplay, MatchResults
from .tournament_manager import TournamentManager
from .menu_manager import MenuManager


class MenuHandler:
    FOLDER_PATH = "src/data"
    TOURNAMENT_FILE = "tournaments.json"
    PLAYER_FILE = "players.json"

    def __init__(self):
        self.menu_manager = MenuManager(self.FOLDER_PATH)
        self.players_data = self.menu_manager.load_data(self.PLAYER_FILE)
        self.tournaments_data = self.menu_manager.load_data(self.TOURNAMENT_FILE)
        self.data_display = DataDisplay(self.players_data, self.tournaments_data)
        self.tournament_manager = TournamentManager()
        self.match_results = MatchResults()

    def handle_tournaments_menu(self, user_choice):
        menu = Menu()

        match user_choice:
            case "1":
                # Liste des tournois
                if self.tournaments_data is None:
                    return "Aucun tournoi enregistré."
                return self.data_display.format_tournaments()

            case "2":
                # Créer un tournoi
                id = self.menu_manager.generate_new_id(self.tournaments_data)
                name = input("Nom: ")
                place = input("Lieu: ")
                start_date = input("Date de début (JJ/MM/AAAA): ")
                end_date = input("Date de fin (JJ/MM/AAAA): ")
                turn = int(input("Nombre de tours (4 par défaut): ")) or 4
                description = (
                    input("Description: ").capitalize() or "Pas de description"
                )

                tournament = Tournament(
                    id, name, place, start_date, end_date, turn, description
                )
                self.tournaments_data.append(tournament.add_tournament())
                self.menu_manager.save_data(self.TOURNAMENT_FILE, self.tournaments_data)

                return "Le tournoi a été ajouté avec succès."

            case "3":
                # Gestion d'un tournoi
                if self.tournaments_data is None:
                    return "Aucun tournoi enregistré."
                print(self.data_display.format_tournaments())

                choice = int(input("\nEntrez l'ID du tournoi à gérer: "))

                for tournament in self.tournaments_data:
                    if tournament["id"] == choice:
                        name = tournament["name"]
                        place = tournament["place"]
                        start_date = tournament["start_date"]
                        end_date = tournament["end_date"]
                        turn = tournament["turn"]
                        print(
                            f"Vous avez choisi le tournoi {name} à {place}\n"
                            f"Date: du {start_date} au {end_date}\nNombre de tours: {turn}"
                        )
                    "Aucun tournoi ne correspond à cet ID."

                sub_choice = menu.tournament_management()
                return self.handle_tournament_management(sub_choice, choice)

            case "4":
                return None

    def handle_players_menu(self, user_choice):
        match user_choice:
            case "1":
                # Afficher la liste des joueurs
                if self.players_data is None:
                    return "Aucun joueur enregistré."
                return self.data_display.format_players()

            case "2":
                # Ajouter un joueur
                id = self.menu_manager.generate_new_id(self.players_data)
                first_name = input("Prénom du joueur: ")
                last_name = input("Nom de famille: ")
                birth_date = input("Date de naissance (JJ/MM/AAAA): ")

                player = Player(id, first_name, last_name, birth_date)
                self.players_data.append(player.add_player())
                self.menu_manager.save_data(self.PLAYER_FILE, self.players_data)

                return "Le joueur a été ajouté avec succès."

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

                turn_number = selected_tournament["turn"]
                for i in range(1, turn_number + 1):
                    current_turn = Turn(f"Round {i}")
                    if current_turn.name == "Round 1":
                        turn = self.tournament_manager.create_turn(
                            current_turn, players
                        )
                        print(turn)
                        self.match_results.display_results(turn)
                    else:
                        turn = self.tournament_manager.create_turn(
                            current_turn, players
                        )
                        print(turn)
                        self.match_results.display_results(turn)

            case "4":
                # Voir les matchs
                return "Matchs affichés."

            case "5":
                return None
