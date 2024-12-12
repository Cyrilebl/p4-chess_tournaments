from src.views import Menu

def main():
  menu = Menu()
  user_choice = menu.choice()
  menu.display(user_choice)

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
