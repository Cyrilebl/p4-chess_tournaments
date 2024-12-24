class PlayerController:
    def __init__(self, player, data_manager, data_view, player_view, message_view):
        self.player = player
        self.data_manager = data_manager
        self.data_view = data_view
        self.player_view = player_view
        self.message_view = message_view
        self.PLAYERS_FILE = "players.json"
        self.players_data = self.data_manager.load_data(self.PLAYERS_FILE)

    def list_player_by_id(self):
        self.message_view.no_current_data(self.players_data)
        self.data_view.format_players(self.players_data, "id")
        self.message_view.return_to_menu()

    def list_player_by_last_name(self):
        self.message_view.no_current_data(self.players_data)
        self.data_view.format_players(self.players_data, "last_name")
        self.message_view.return_to_menu()

    def add_player(self):
        id = self.data_manager.generate_new_id(self.players_data)
        first_name, last_name, birth_date = self.player_view.get_player_data()
        new_player = self.player(id, first_name, last_name, birth_date)
        self.players_data.append(new_player.serialize())
        self.data_manager.save_data(self.PLAYERS_FILE, self.players_data)
        self.message_view.new_entity_success("joueur")
        self.message_view.return_to_menu()
