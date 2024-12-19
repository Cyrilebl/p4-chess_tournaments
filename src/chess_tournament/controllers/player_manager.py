from src.chess_tournament.models import Player


class PlayerManager:
    def list_player(self, players_data, data_display):
        if players_data is None:
            return "Aucun joueur enregistré."
        return data_display.format_players()

    def create_player(self, player_file, players_data, data_manager):
        id = data_manager.generate_new_id(players_data)
        first_name = input("Prénom du joueur: ")
        last_name = input("Nom de famille: ")
        birth_date = input("Date de naissance (JJ/MM/AAAA): ")

        player = Player(id, first_name, last_name, birth_date)
        players_data.append(player.add_player())
        data_manager.save_data(player_file, players_data)

        return "Le joueur a été ajouté avec succès."
