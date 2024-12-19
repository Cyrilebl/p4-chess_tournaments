import random
from src.chess_tournament.models import Turn, Match


class TournamentManager:
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
