import datetime


class Turn:
    def __init__(self, name):
        self.name = name
        self.start_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.end_date = None
        self.scores_updated = False
        self.matches = []

    def end_turn(self):
        self.end_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self.end_date

    def serialize(self):
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "scores_updated": self.scores_updated,
            "matches": self.matches,
        }
