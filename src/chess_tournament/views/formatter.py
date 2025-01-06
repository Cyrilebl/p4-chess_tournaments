from tabulate import tabulate


class Formatter:
    def format_players(self, players_data, sort_filter):
        if not players_data:
            return print("\nAucun joueur enregistré.")

        headers = ["ID", "Nom", "Prénom", "Date de naissance"]
        rows = []

        sorted_players = sorted(players_data, key=lambda player: player[sort_filter])

        for player in sorted_players:
            rows.append(
                [
                    player["id"],
                    player["last_name"],
                    player["first_name"],
                    player["birth_date"],
                ]
            )

        return print(tabulate(rows, headers, tablefmt="grid"))

    def format_tournaments(self, tournaments_data):
        if not tournaments_data:
            return print("\nAucun tournoi enregistré.")

        headers = [
            "ID",
            "Nom",
            "Lieu",
            "Date de début",
            "Date de fin",
            "Tours",
            "Description",
        ]
        rows = []

        for tournament in tournaments_data:
            rows.append(
                [
                    tournament["id"],
                    tournament["name"],
                    tournament["place"],
                    tournament["start_date"],
                    tournament["end_date"],
                    tournament["turn"],
                    tournament["description"],
                ]
            )

        return print(tabulate(rows, headers, tablefmt="grid"))

    def format_tournament_players(self, players_data, selected_tournament, sort_filter):
        players_dict = self.get_players_dict(players_data)

        tournament_players = selected_tournament.get("players", [])
        if not tournament_players:
            return print("\nAucun joueur enregistré dans ce tournoi.")

        headers = ["ID", "Nom", "Prénom", "Date de naissance", "Score"]
        rows = []
        if sort_filter == "score":
            sorted_players = sorted(
                tournament_players,
                key=lambda player: next(
                    (p["score"] for p in tournament_players if p["id"] == player["id"])
                ),
                reverse=True,
            )
        else:
            sorted_players = sorted(
                tournament_players,
                key=lambda player: players_dict.get(player["id"]).get(sort_filter),
            )

        for player in sorted_players:
            id = player["id"]
            score = player["score"]
            player_details = players_dict.get(id)

            rows.append(
                [
                    id,
                    player_details["last_name"],
                    player_details["first_name"],
                    player_details["birth_date"],
                    score,
                ]
            )
        return print(tabulate(rows, headers, tablefmt="grid"))

    def get_players_dict(self, players_data):
        return {player["id"]: player for player in players_data}

    def get_rounds_data(self, selected_tournament):
        rounds_data = selected_tournament.get("rounds", [])
        if not rounds_data:
            print("\nAucun match n'existe pour ce tournoi")
            return None
        return rounds_data

    def format_round(self, round_name, round_data, players_dict):
        print(f"\n--- {round_name} ---")

        matches_data = round_data.get("matches", [])

        for index, match in enumerate(matches_data, start=1):
            first_player_id, second_player_id = match[0]
            first_player_score, second_player_score = match[1]

            first_player = players_dict.get(first_player_id)
            second_player = players_dict.get(second_player_id)

            if second_player_id == -1:
                print(
                    f"{first_player['last_name']} {first_player['first_name']} ({first_player_score})"
                    f" obtient un bye pour ce tour."
                )
            else:
                print(
                    f"Match {index}: "
                    f"{first_player['last_name']} {first_player['first_name']} ({first_player_score})"
                    f" vs "
                    f"{second_player['last_name']} {second_player['first_name']} ({second_player_score})"
                )

    def format_all_rounds(self, players_data, selected_tournament):
        players_dict = self.get_players_dict(players_data)
        rounds_data = self.get_rounds_data(selected_tournament)

        if not rounds_data:
            return False

        for index, round in enumerate(rounds_data, start=1):
            round_name = round.get("name")
            self.format_round(round_name, round, players_dict)

        return True

    def format_last_round(self, players_data, selected_tournament):
        players_dict = self.get_players_dict(players_data)
        rounds_data = self.get_rounds_data(selected_tournament)

        if not rounds_data:
            return False

        last_round = rounds_data[-1]
        round_name = last_round.get("name")
        self.format_round(round_name, last_round, players_dict)

        return True
