class Game:
  def __init__(self, win, defeat, null):
    self.win = win
    self.defeat = defeat
    self.null = null
    
  def result(self):
    if self.win:
      score += 1
    elif self.defeat:
      score = score
    elif self.null:
      score += 0.5
