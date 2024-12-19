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

    def __str__(self):
        return "\n".join(str(match) for match in self.matches)
