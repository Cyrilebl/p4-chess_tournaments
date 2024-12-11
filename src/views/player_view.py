import json
from tabulate import tabulate

def load_data(file_path):
  with open(file_path, "r") as file:
    return json.load(file)
      
def display_players(players_data):
  headers = ["Nom", "Prénom", "Date de naissance"]
  rows = []
  
  for player in players_data:
    rows.append([player['last_name'], player['first_name'], player['birth_date']])
    output = tabulate(rows, headers, tablefmt="grid")
    
  return output