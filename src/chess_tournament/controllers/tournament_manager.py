import random
from src.chess_tournament.models import Turn, Match, Tournament


class TournamentManager:
    def __init__(self, tournament_file, tournaments_data, data_display, data_manager):
        self.tournament_file = tournament_file
        self.tournaments_data = tournaments_data
        self.data_display = data_display
        self.data_manager = data_manager

    def list_tournament(self):
        if self.tournaments_data is None:
            return "Aucun tournoi enregistré."
        return self.data_display.format_tournaments()

    def create_tournament(self):
        id = self.data_manager.generate_new_id(self.tournaments_data)
        name = input("Nom: ")
        place = input("Lieu: ")
        start_date = input("Date de début (JJ/MM/AAAA): ")
        end_date = input("Date de fin (JJ/MM/AAAA): ")
        turn = input("Nombre de tours (4 par défaut): ") or 4
        description = input("Description: ").capitalize() or "Pas de description"

        tournament = Tournament(
            id, name, place, start_date, end_date, turn, description
        )
        self.tournaments_data.append(tournament.add_tournament())
        self.data_manager.save_data(self.tournament_file, self.tournaments_data)

        return "Le tournoi a été ajouté avec succès."

    def manage_tournament(self):
        print(self.list_tournament())

        while True:
            try:
                choice = int(input("\nEntrez l'ID du tournoi à gérer: "))
                if 1 <= choice <= len(self.tournaments_data):
                    break
                else:
                    print("L'ID n'est pas valide, veuillez réessayer")
            except ValueError:
                print("Veuillez entrer un ID valide")

        return choice

    def update_player_score(self, tournament, updated_scores):
        for player in tournament["players"]:
            for updated_player in updated_scores:
                if (
                    player["first_name"] == updated_player["first_name"]
                    and player["last_name"] == updated_player["last_name"]
                ):
                    player["score"] = updated_player["score"]

    def create_turn(sort_players):
        def wrapper(self, turn_name, players):
            sort_players(self, players)

            turn = Turn(turn_name)

            if len(players) % 2 != 0:
                bye_player = players.pop()
                print(
                    f"\n{bye_player['last_name']}{bye_player['first_name']} obtient un bye pour ce tour."
                )

            for i in range(0, len(players), 2):
                first_player = players[i]
                second_player = players[i + 1]
                match = Match(first_player, second_player)
                turn.add_match(match.set_match())

            return turn

        return wrapper

    @create_turn
    def shuffle(self, players):
        random.shuffle(players)

    @create_turn
    def sort_by_score(self, players):
        return players.sort(key=lambda player: player["score"], reverse=True)

    def already_play():
        pass

    # if first_player already play against second_player skip
