from datetime import datetime


class Player:
    def __init__(self, id, first_name, last_name, birth_date):
        self.id = id
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

        try:
            self.birth_date = datetime.strptime(birth_date, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("La date de naissance doit être au format JJ/MM/AAAA.")

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date.strftime("%d/%m/%Y"),
        }
