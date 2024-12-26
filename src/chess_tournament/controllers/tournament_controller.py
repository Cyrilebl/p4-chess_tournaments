class TournamentController:
    def __init__(
        self, tournament, data_manager, data_view, tournament_view, message_view
    ):
        self.tournament = tournament
        self.data_manager = data_manager
        self.data_view = data_view
        self.tournament_view = tournament_view
        self.message_view = message_view
        self.TOURNAMENTS_FILE = "tournaments.json"
        self.tournaments_data = self.data_manager.load_data(self.TOURNAMENTS_FILE)

    def list_tournament(self):
        self.data_view.format_tournaments(self.tournaments_data)
        self.message_view.return_to_menu()

    def add_tournament(self):
        id = self.data_manager.generate_new_id(self.tournaments_data)
        name, place, start_date, end_date, turn, description = (
            self.tournament_view.get_tournament_data()
        )
        new_tournament = self.tournament(
            id, name, place, start_date, end_date, turn, description
        )
        self.tournaments_data.append(new_tournament.serialize())
        self.data_manager.save_data(self.TOURNAMENTS_FILE, self.tournaments_data)
        self.message_view.new_entity_success("tournoi")
        self.message_view.return_to_menu()
