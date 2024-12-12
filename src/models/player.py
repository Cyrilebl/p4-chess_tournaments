from datetime import datetime

class Player:
  def __init__(self, first_name, last_name, birth_date ):    
    self.first_name = first_name.capitalize()
    self.last_name = last_name.capitalize()
    
    try:
        self.birth_date = datetime.strptime(birth_date, "%d/%m/%Y").date()
    except ValueError:
        raise ValueError("La date de naissance doit être au format JJ/MM/AAAA.")

  def add_player(self):
    return {      
      "first_name": self.first_name,
      "last_name": self.last_name,
      "birth_date": self.birth_date.strftime("%d/%m/%Y"),
    }
    
    #modifier un joueur
  def __str__(self):
   return (    
    f"Prénom: {self.first_name}\n"
    f"Nom: {self.last_name}\n"
    f"Date de naissance: {self.birth_date.strftime('%d/%m/%Y')}\n"
    )