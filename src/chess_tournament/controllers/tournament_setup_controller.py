class TournamentSetupController:
    def __init__(
        self,
        tournament,
        turn,
        data_manager,
        data_view,
        message_view,
        tournament_view,
        matches_view,
        helpers_view,
        round_controller,
    ):
        self.tournament = tournament
        self.turn = turn
        self.data_manager = data_manager
        self.data_view = data_view
        self.message_view = message_view
        self.tournament_view = tournament_view
        self.matches_view = matches_view
        self.helpers_view = helpers_view
        self.players_data = self.data_manager.load_data(data_manager.PLAYERS_FILE)
        self.tournaments_data = self.data_manager.load_data(
            data_manager.TOURNAMENTS_FILE
        )
        self.round_controller = round_controller

    def tournament_choice(self):
        self.data_view.format_tournaments(self.tournaments_data)

        while True:
            user_choice = self.message_view.ask_tournament_id()
            tournament = self.helpers_view.find_element_by_id(
                user_choice, self.tournaments_data
            )
            if tournament:
                return tournament

    def add_player(self, selected_tournament):
        self.data_view.format_players(self.players_data, "id")

        while True:
            user_choice = self.message_view.ask_player_id()
            if user_choice.lower() == "q":
                break

            player = self.helpers_view.find_element_by_id(
                user_choice, self.players_data
            )

            selected_tournament.setdefault("players", [])

            if any(
                existing_player["id"] == player["id"]
                for existing_player in selected_tournament["players"]
            ):
                self.message_view.player_already_registered()
            else:
                selected_tournament["players"].append({"id": player["id"], "score": 0})
                self.message_view.new_entity_success("joueur")

        self.data_manager.save_data(
            self.data_manager.TOURNAMENTS_FILE, self.tournaments_data
        )

    def list_tournament_players(self, selected_tournament):
        self.data_view.format_tournament_players(
            self.players_data, selected_tournament, "last_name"
        )
        self.message_view.return_to_menu()

    def generate_matches(self, selected_tournament):
        number_of_turns = selected_tournament["turn"]
        rounds = selected_tournament.setdefault("rounds", [])

        if len(rounds) >= number_of_turns:
            self.message_view.can_t_generate_more_matches()
            return self.message_view.return_to_menu()

        if rounds and not rounds[-1]["scores_updated"]:
            self.message_view.record_scores()
            return self.message_view.return_to_menu()

        current_round_name = f"Round {len(rounds) + 1}"
        new_round = self.turn(current_round_name)

        try:
            if not rounds:
                matches = self.round_controller.shuffle(selected_tournament)
            else:
                matches = self.round_controller.sort_by_score(selected_tournament)
        except KeyError:
            self.message_view.no_player()
            return self.message_view.return_to_menu()

        serialized_round = new_round.serialize()
        serialized_round["matches"] = matches
        rounds.append(serialized_round)

        self.data_view.format_last_round(self.players_data, selected_tournament)
        self.data_manager.save_data(
            self.data_manager.TOURNAMENTS_FILE, self.tournaments_data
        )

        self.message_view.return_to_menu()

    def list_matches(self, selected_tournament):
        self.data_view.format_all_rounds(self.players_data, selected_tournament)
        self.message_view.return_to_menu()

    def register_score(self, selected_tournament):
        if not self.data_view.format_last_round(self.players_data, selected_tournament):
            return self.message_view.return_to_menu()

        current_round = selected_tournament["rounds"][-1]

        if current_round["scores_updated"]:
            self.message_view.scores_already_updated()
            return self.message_view.return_to_menu()

        self.matches_view.scoring(
            current_round["matches"], self.players_data, selected_tournament
        )
        current_round["scores_updated"] = True
        current_round["end_date"] = self.turn(current_round["name"]).end_turn()

        self.data_view.format_last_round(self.players_data, selected_tournament)
        self.data_manager.save_data(
            self.data_manager.TOURNAMENTS_FILE, self.tournaments_data
        )
        self.message_view.return_to_menu()

    def ranking(self, selected_tournament):
        self.data_view.format_tournament_players(
            self.players_data, selected_tournament, "score"
        )
        self.message_view.return_to_menu()
