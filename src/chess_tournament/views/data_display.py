from tabulate import tabulate


class DataDisplay:
    def __init__(self, players_data, tournaments_data):
        self.players_data = players_data
        self.tournaments_data = tournaments_data

    def format_players(self):
        headers = ["ID", "Nom", "Prénom", "Date de naissance"]
        rows = []

        sorted_players = sorted(
            self.players_data, key=lambda player: player["last_name"]
        )

        for player in sorted_players:
            rows.append(
                [
                    player["id"],
                    player["last_name"],
                    player["first_name"],
                    player["birth_date"],
                ]
            )
        return tabulate(rows, headers, tablefmt="grid")

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
