from tabulate import tabulate
               
def display_players(players_data):
    headers = ["ID", "Nom", "Prénom", "Date de naissance"]
    rows = []

    for player in players_data:
        rows.append([player["id"], player['last_name'], player['first_name'], player['birth_date']])

    return tabulate(rows, headers, tablefmt="grid")

def display_tournaments(tournaments_data):
    headers = ["ID", "Nom", "Lieu", "Date de début", "Date de fin", "Tours", "Description"]
    rows = []

    for tournament in tournaments_data:
        rows.append([tournament['id'], tournament['name'], tournament['place'], tournament['start_date'], tournament['end_date'], tournament['turn'], tournament['description']])

    return tabulate(rows, headers, tablefmt="grid")
    