import os
import json
from tabulate import tabulate
         
def load_data(folder_path, file_name):
  
  # Ensure the folder exists
  os.makedirs(folder_path, exist_ok=True)
  
  # Construct the full file path
  full_path = os.path.join(folder_path, file_name)
  
  if os.path.exists(full_path):
    with open(full_path, "r") as file:
      return json.load(file)
      
def display_players(players_data):
  headers = ["Nom", "Prénom", "Date de naissance"]
  rows = []
  
  for player in players_data:
    rows.append([player['last_name'], player['first_name'], player['birth_date']])
  
  return tabulate(rows, headers, tablefmt="grid")
    