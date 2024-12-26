import datetime


class Turn:
    def __init__(self, name):
        self.name = name
        self.start_date = datetime.datetime.now()
        self.end_date = None
        self.matches = []

    def end_turn(self):
        self.end_date = datetime.datetime.now()

    def serialize(self):
        return {
            "name": self.name,
            "start_date": self.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            "end_date": (
                self.end_date.strftime("%Y-%m-%d %H:%M:%S") if self.end_date else None
            ),
            "matches": self.matches,
        }
