from src.chess_tournament.models import Player


class PlayerManager:
    def __init__(self, player_file, players_data, data_display, data_manager):
        self.player_file = player_file
        self.players_data = players_data
        self.data_display = data_display
        self.data_manager = data_manager

    def list_player_by_id(self):
        if self.players_data is None:
            return "Aucun joueur enregistré."
        return self.data_display.format_players("id")

    def list_player_by_last_name(self):
        if self.players_data is None:
            return "Aucun joueur enregistré."
        return self.data_display.format_players("last_name")

    def create_player(self):
        id = self.data_manager.generate_new_id(self.players_data)
        first_name = input("Prénom du joueur: ")
        last_name = input("Nom de famille: ")
        birth_date = input("Date de naissance (JJ/MM/AAAA): ")

        player = Player(id, first_name, last_name, birth_date)
        self.players_data.append(player.add_player())
        self.data_manager.save_data(self.player_file, self.players_data)

        return "Le joueur a été ajouté avec succès."
