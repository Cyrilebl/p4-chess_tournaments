from src.chess_tournament.models.element_manager import find_element_by_id


class TournamentSetupController:
    def __init__(
        self, tournament, data_manager, data_view, tournament_view, message_view
    ):
        self.tournament = tournament
        self.data_manager = data_manager
        self.data_view = data_view
        self.tournament_view = tournament_view
        self.message_view = message_view
        self.PLAYERS_FILE = "players.json"
        self.TOURNAMENTS_FILE = "tournaments.json"
        self.players_data = self.data_manager.load_data(self.PLAYERS_FILE)
        self.tournaments_data = self.data_manager.load_data(self.TOURNAMENTS_FILE)

    def tournament_choice(self):
        self.message_view.no_current_data(self.tournaments_data)
        self.data_view.format_tournaments(self.tournaments_data)

        while True:
            try:
                user_choice = self.message_view.ask_tournament_id()
                tournament = find_element_by_id(self.tournaments_data, user_choice)
                if tournament:
                    return tournament
                self.message_view.invalid_id()
            except ValueError:
                self.message_view.invalid_id()

    def add_player(self, selected_tournament):
        self.message_view.no_current_data(self.players_data)
        self.data_view.format_players(self.players_data, "id")

        while True:
            try:
                user_choice = self.message_view.ask_player_id()
                if user_choice.lower() == "q":
                    break

                player = find_element_by_id(self.players_data, user_choice)
                selected_tournament.setdefault("players", [])

                if any(
                    existing_player["id"] == player["id"]
                    for existing_player in selected_tournament["players"]
                ):
                    self.message_view.player_already_registered()
                else:
                    selected_tournament["players"].append(player)
            except (ValueError, TypeError):
                self.message_view.invalid_id()

        self.data_manager.save_data(self.TOURNAMENTS_FILE, self.tournaments_data)

    def list_tournament_players(self, selected_tournament):
        players_data = selected_tournament.get("players", [])

        if players_data:
            self.data_view.format_players(players_data, "id")
        else:
            self.message_view.no_current_data()
        self.message_view.return_to_menu()

    def list_matches(self, selected_tournament):
        matches_data = selected_tournament.get("matches", [])

        if matches_data:
            self.data_view.format_matches(matches_data)
        else:
            self.message_view.no_current_data()
        self.message_view.return_to_menu()

    def generate_matches(self, selected_tournament):
        try:
            players = selected_tournament["players"]
        except KeyError:
            return "Aucun joueur dans ce tournoi."

        if "matches" not in selected_tournament:
            selected_tournament["matches"] = []

        turn_number = int(selected_tournament["turn"])
        for i in range(1, turn_number + 1):
            print(f"\nRound {i} - Match:")

            if i == 1:
                create_turn = self.tournament_manager.shuffle(f"Round {i}", players)
            else:
                create_turn = self.tournament_manager.sort_by_score(
                    f"Round {i}", players
                )

            print(create_turn)
            self.match_results.display_turn_matches(create_turn)
            create_turn.end_turn()
            selected_tournament["matches"].append(create_turn.to_dict())

            self.tournament_manager.update_player_score(selected_tournament, players)
            self.data_manager.save_data(self.TOURNAMENT_FILE, self.tournaments_data)

        return "Match terminés."
