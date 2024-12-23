import datetime


class Turn:
    def __init__(self, name):
        self.name = name
        self.start_date = datetime.datetime.now()
        self.end_date = None
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def end_turn(self):
        self.end_date = datetime.datetime.now()

    def to_dict(self):
        return {
            "name": self.name,
            "start_date": self.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            "end_date": (
                self.end_date.strftime("%Y-%m-%d %H:%M:%S") if self.end_date else None
            ),
            "matches": self.matches,
        }

    def __str__(self):
        match_strings = []
        for match in self.matches:
            first_player = match[0][0]
            second_player = match[1][0]

            match_strings.append(
                f"{first_player['first_name']} {first_player['last_name']} ({first_player['score']}) "
                f"vs "
                f"{second_player['first_name']} {second_player['last_name']} ({second_player['score']})"
            )

        return "\n".join(match_strings)
