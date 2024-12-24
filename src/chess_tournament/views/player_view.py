class PlayerView:
    def get_player_data(self):
        first_name = input("Prénom du joueur: ")
        last_name = input("Nom de famille: ")
        birth_date = input("Date de naissance (JJ/MM/AAAA): ")

        return first_name, last_name, birth_date
