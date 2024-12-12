import os
import json
from tabulate import tabulate
               
def display_players(players_data):
  headers = ["Nom", "Prénom", "Date de naissance"]
  rows = []
  
  for player in players_data:
    rows.append([player['last_name'], player['first_name'], player['birth_date']])
  
  return tabulate(rows, headers, tablefmt="grid")
    