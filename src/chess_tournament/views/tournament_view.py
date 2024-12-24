class TournamentView:
    def get_tournament_data(self):
        name = input("Nom: ")
        place = input("Lieu: ")
        start_date = input("Date de début (JJ/MM/AAAA): ")
        end_date = input("Date de fin (JJ/MM/AAAA): ")
        turn = input("Nombre de tours (4 par défaut): ") or 4
        description = input("Description: ").capitalize() or "Pas de description"

        return name, place, start_date, end_date, turn, description
