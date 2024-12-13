class Match:
  def __init__(self, first_player, second_player, win, defeat, null):
    self.first_player = first_player
    self.second_player = second_player
    self.matches = []
    
    self.win = win
    self.defeat = defeat
    self.null = null
  
  def set_match(self):
    match = (
    f"{self.first_player['last_name']}, {self.first_player['first_name']}", self.first_player["score"],
    f"{self.second_player['last_name']}, {self.second_player['first_name']}", self.second_player["score"])
    
    self.matches.append(match)
  
  def result(self):
    if self.win:
      score += 1
    elif self.defeat:
      score = score
    elif self.null:
      score += 0.5
