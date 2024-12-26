import datetime


class Turn:
    def __init__(self, name):
        self.name = name
        self.start_date = datetime.datetime.now()
        self.end_date = None
        self.matches = []

    def end_turn(self):
        self.end_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self.end_date

    def serialize(self):
        return {
            "name": self.name,
            "start_date": self.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            "end_date": None,
            "matches": self.matches,
        }
