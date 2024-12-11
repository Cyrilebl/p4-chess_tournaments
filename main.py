from src.views import Menu
from src.models import Player
from src.controllers import save_to_json

def main():
  player1 = Player("pierre", "dufour", "08/11/2002")
  player2 = Player("john", "doe", "08/11/1988")

  players_data = [player1.to_dict(), player2.to_dict()]
  save_to_json("src/data", "players.json", players_data)

  menu = Menu()
  user_choice = menu.choice()
  result = menu.display(user_choice)
  
  print(result)

if __name__ == "__main__":
  main()

# Chaque tour est une liste de matchs.
# Chaque match consiste en une paire de joueurs.

# nombre de tours – réglez la valeur par défaut sur 4
# numéro correspondant au tour actuel
# une liste des tours
# une liste des joueurs enregistrés
# description pour les remarques générales du directeur du tournoi.

class Turns:
  def __init__(self):
    pass
