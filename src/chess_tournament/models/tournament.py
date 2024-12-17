from datetime import datetime
# numéro correspondant au tour actuel
# une liste des tours
# une liste des joueurs enregistrés

class Tournament:
    def __init__(self, id, name, place, start_date, end_date, turn, description):
        self.id = id
        self.name = name.title()
        self.place = place.capitalize()
        
        try:
            self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
            self.end_date = datetime.strptime(end_date, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("La date doit être au format JJ/MM/AAAA.")
        
        self.turn = turn
        self.description = description
        
    def add_tournament(self):
        return {
        "id": self.id,
        "name": self.name,
        "place": self.place,
        "start_date": self.start_date.strftime("%d/%m/%Y"),
        "end_date": self.end_date.strftime("%d/%m/%Y"),
        "turn": self.turn,
        "description": self.description,
        }
    