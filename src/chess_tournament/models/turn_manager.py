import random


class TurnManager:
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

            # turn = Turn(turn_name)

            if len(players) % 2 != 0:
                bye_player = players.pop()
                print(
                    f"\n{bye_player['last_name']}{bye_player['first_name']} obtient un bye pour ce tour."
                )

            for i in range(0, len(players), 2):
                first_player = players[i]
                second_player = players[i + 1]
            #   match = Match(first_player, second_player)
            #   turn.add_match(match.set_match())

        #   return turn

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
