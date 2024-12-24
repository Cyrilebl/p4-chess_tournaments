from tabulate import tabulate


class DisplayData:
    def format_players(self, players_data, sort_filter):
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

    def format_tournaments(self):
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

        for tournament in self.tournaments_data:
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

        return tabulate(rows, headers, tablefmt="grid")

    def format_tournament_players(self, players_data):
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
        return tabulate(rows, headers, tablefmt="grid")
