import random


class MatchMaker:
    def has_played(self, player1_id, player2_id, rounds_data):
        for round_data in rounds_data:
            for match in round_data["matches"]:
                match_players = match[0]
                if {player1_id, player2_id} == set(match_players):
                    return True
        return False

    def generate_round(sort_players):
        def wrapper(self, selected_tournament):
            players = selected_tournament["players"]
            rounds_data = selected_tournament.get("rounds", [])

            sort_players(self, players)

            matches = []
            bye_player = None

            if len(players) % 2 != 0:
                bye_player = players[-1]
                bye_player["score"] += 1

                players = players[:-1]

            for i in range(0, len(players), 2):
                first_player = players[i]
                second_player = players[i + 1]

                while self.has_played(
                    first_player["id"], second_player["id"], rounds_data
                ):
                    second_player = next(
                        (
                            player
                            for player in players
                            if player != first_player
                            and not self.has_played(
                                first_player["id"], player["id"], rounds_data
                            )
                        ),
                        second_player,
                    )
                matches.append([[first_player["id"], second_player["id"]], [0, 0]])

            if bye_player:
                matches.append([[bye_player["id"], -1], [1, 0]])

            return matches

        return wrapper

    @generate_round
    def shuffle(self, players):
        random.shuffle(players)
        return players

    @generate_round
    def sort_by_score(self, players):
        players.sort(key=lambda player: player["score"], reverse=True)
        return players
