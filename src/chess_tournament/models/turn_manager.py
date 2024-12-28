import random


class TurnManager:
    def update_players_scores(self, tournament):
        last_round = tournament["rounds"][-1]

        for match in last_round["matches"]:
            first_player, second_player = match

            for player in tournament["players"]:
                if player["id"] == first_player["id"]:
                    player["score"] = first_player["score"]
                elif player["id"] == second_player["id"]:
                    player["score"] = second_player["score"]

    def create_turn(sort_players):
        def wrapper(self, selected_tournament):
            players = selected_tournament["players"]

            sort_players(self, players)
            matches = []

            if len(players) % 2 != 0:
                bye_player = players.pop()
                bye_player["score"] += 1
                print(
                    f"\n{bye_player['last_name']}{bye_player['first_name']} obtient un bye pour ce tour."
                )

            for i in range(0, len(players), 2):
                first_player = players[i]
                second_player = players[i + 1]
                matches.append((first_player, second_player))

            return matches

        return wrapper

    @create_turn
    def shuffle(self, players):
        random.shuffle(players)
        return players

    @create_turn
    def sort_by_score(self, players):
        players.sort(key=lambda player: player["score"], reverse=True)
        return players

    def already_play():
        pass

    # if first_player already play against second_player skip
