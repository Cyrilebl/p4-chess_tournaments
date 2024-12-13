class Match:
  def __init__(self, first_player, second_player):
    self.first_player = first_player
    self.second_player = second_player
  
  def set_match(self):
    return (
      f"{self.first_player['last_name']}, {self.first_player['first_name']}", self.first_player["score"],
      f"{self.second_player['last_name']}, {self.second_player['first_name']}", self.second_player["score"]
      )
    
  # At the end of a match user select first_player winner, second_player winner or draw (3 choices)
  def result(self, result):
    if result == "first_wins":
      self.first_player.score += 1
    elif result == "second_wins":
      self.second_player += 1
    elif result == "draw":
      self.first_player.score += 0.5
      self.second_player.score += 0.5

  def __str__(self):
    return f"{self.first_player} vs {self.second_player}"
