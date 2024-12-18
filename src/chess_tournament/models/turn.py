# Chaque tour est une liste de matchs.
# Noms : Round 1, Round 2 ...
# Un champ Date et heure de début
# Un champ Date et heure de fin
# Les champs doivent être automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé


class Turn:
    def __init__(self, name):
        self.name = name
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    # À faire
    def __str__(self):
        return f"{self.name}:\n" + "\n".join([str(match) for match in self.matches])
