from datetime import datetime
# Un tournoi a un nombre de tours défini.
class Tournament:
  def __init__(self, name, place, start_date, end_date):
    self.name = name.capitalize()
    self.place = place.capitalize()
    
    try:
      self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
      self.end_date = datetime.strptime(end_date, "%d/%m/%Y").date()
    except ValueError:
      raise ValueError("La date doit être au format JJ/MM/AAAA.")
    
  def add_tournament(self):
    return {
      "name": self.name,
      "place": self.place,
      "start_date": self.start_date.strftime("%d/%m/%Y"),
      "end_date": self.end_date.strftime("%d/%m/%Y"),
    }