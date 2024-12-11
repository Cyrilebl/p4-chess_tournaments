# Un tournoi a un nombre de tours défini.

class Tournament:
  def __init__(self, name, place, start_date, end_date):
    self.name = name
    self.place = place
    self.start_date = start_date
    self.end_date = end_date
    
    #genere tournament.json