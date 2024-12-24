class PlayerManager:
    def list_player_by_id(self):
        if self.players_data is None:
            return "Aucun joueur enregistré."
        return self.data_display.format_players("id")

    def list_player_by_last_name(self):
        if self.players_data is None:
            return "Aucun joueur enregistré."
        return self.data_display.format_players("last_name")
