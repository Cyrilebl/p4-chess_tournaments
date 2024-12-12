# Chaque tour est une liste de matchs.
# Chaque match consiste en une paire de joueurs.

# nombre de tours – réglez la valeur par défaut sur 4
# numéro correspondant au tour actuel
# une liste des tours
# une liste des joueurs enregistrés
# description pour les remarques générales du directeur du tournoi.

class Turn:
  def __init__(self, first_player, second_player,):
    self.first_player = first_player
    self.second_player = second_player
