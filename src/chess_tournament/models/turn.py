# Un champ Date et heure de début
# Un champ Date et heure de fin
# Les champs doivent être automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé


class Turn:
    def __init__(self, name):
        self.name = name
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def __str__(self):
        matches_str = "\n".join([str(match) for match in self.matches])
        return f"\n{self.name} - Matches :\n{matches_str}"
