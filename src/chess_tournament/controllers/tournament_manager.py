import random
from src.chess_tournament.models import Turn, Match, Tournament


class TournamentManager:
    def list_tournament(self, tournaments_data, data_display):
        if tournaments_data is None:
            return "Aucun tournoi enregistré."
        return data_display.format_tournaments()

    def create_tournament(self, tournament_file, tournaments_data, data_manager):
        id = data_manager.generate_new_id(tournaments_data)
        name = input("Nom: ")
        place = input("Lieu: ")
        start_date = input("Date de début (JJ/MM/AAAA): ")
        end_date = input("Date de fin (JJ/MM/AAAA): ")
        turn = input("Nombre de tours (4 par défaut): ") or 4
        description = input("Description: ").capitalize() or "Pas de description"

        tournament = Tournament(
            id, name, place, start_date, end_date, turn, description
        )
        tournaments_data.append(tournament.add_tournament())
        data_manager.save_data(tournament_file, tournaments_data)

        return "Le tournoi a été ajouté avec succès."

    def manage_tournament(
        self, tournaments_data, data_display, menu, handle_tournament_management
    ):
        print(self.list_tournament(tournaments_data, data_display))

        choice = int(input("\nEntrez l'ID du tournoi à gérer: "))

        for tournament in tournaments_data:
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
        return handle_tournament_management(sub_choice, choice)

    def create_turn(self, turn_name, players):
        random.shuffle(players)
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
            turn.add_match(match)

        return turn
