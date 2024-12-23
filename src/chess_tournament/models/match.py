class Match:
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player

    def set_match(self):
        return (
            [self.first_player],
            [self.second_player],
        )

    def __str__(self):
        return f"{self.first_player['last_name']} {self.first_player['first_name']} vs {self.second_player['last_name']} {self.second_player['first_name']} : {self.first_player['score']} - {self.second_player['score']}"
