from tabulate import tabulate


class DisplayData:
    def format_players(self, players_data, sort_filter):
        try:
            players_data
        except FileNotFoundError:
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
        try:
            tournaments_data
        except FileNotFoundError:
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

    def format_tournament_players(self, selected_tournament):
        try:
            players_data = selected_tournament["players"]
        except KeyError:
            return print("\nAucun joueur enregistré dans ce tournoi.")

        headers = ["ID", "Nom", "Prénom", "Date de naissance", "Score"]
        rows = []

        sorted_players = sorted(
            players_data, key=lambda player: player["score"], reverse=True
        )

        for player in sorted_players:
            rows.append(
                [
                    player["id"],
                    player["last_name"],
                    player["first_name"],
                    player["birth_date"],
                    player["score"],
                ]
            )
        return print(tabulate(rows, headers, tablefmt="grid"))

    def format_matches(self, selected_tournament):
        try:
            rounds_data = selected_tournament["rounds"]
        except KeyError:
            return print("\nAucun match n'existe pour ce tournoi")

        for index, round in enumerate(rounds_data, start=1):
            round_name = round.get("name", f"Round {index}")
            print(f"\n--- {round_name} ---")

            matches_data = round.get("matches", [])

            for index, match in enumerate(matches_data, start=1):
                first_player, second_player = match
                print(
                    f"Match {index}: "
                    f"{first_player['last_name']} {first_player['first_name']} ({first_player['score']})"
                    f" vs "
                    f"{second_player['last_name']} {second_player['first_name']} ({second_player['score']})"
                )
