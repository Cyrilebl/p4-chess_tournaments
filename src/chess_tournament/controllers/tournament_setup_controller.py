class TournamentSetupController:
    def __init__(
        self,
        tournament,
        turn,
        data_manager,
        turn_manager,
        data_view,
        message_view,
        tournament_view,
        matches_view,
        helpers_view,
    ):
        self.tournament = tournament
        self.turn = turn
        self.data_manager = data_manager
        self.turn_manager = turn_manager
        self.data_view = data_view
        self.message_view = message_view
        self.tournament_view = tournament_view
        self.matches_view = matches_view
        self.helpers_view = helpers_view
        self.players_data = self.data_manager.load_data(data_manager.PLAYERS_FILE)
        self.tournaments_data = self.data_manager.load_data(
            data_manager.TOURNAMENTS_FILE
        )

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
                selected_tournament["players"].append(player)
                self.message_view.new_entity_success("joueur")

        self.data_manager.save_data(
            self.data_manager.TOURNAMENTS_FILE, self.tournaments_data
        )

    def list_tournament_players(self, selected_tournament):
        self.data_view.format_tournament_players(selected_tournament)
        self.message_view.return_to_menu()

    def generate_matches(self, selected_tournament):
        number_of_turns = selected_tournament["turn"]
        rounds = selected_tournament.setdefault("rounds", [])

        if len(rounds) >= number_of_turns:
            self.message_view.can_t_generate_more_matches()
            return self.message_view.return_to_menu()

        if rounds and rounds[-1]["scores_updated"] == False:
            self.message_view.record_scores()
            return self.message_view.return_to_menu()

        current_round_name = f"Round {len(rounds) + 1}"
        new_round = self.turn(current_round_name)

        try:
            if not rounds:
                matches = self.turn_manager.shuffle(selected_tournament)
            else:
                matches = self.turn_manager.sort_by_score(selected_tournament)
        except KeyError:
            self.message_view.no_player()
            return self.message_view.return_to_menu()

        serialized_round = new_round.serialize()
        serialized_round["matches"] = matches
        rounds.append(serialized_round)

        self.data_view.format_matches(selected_tournament)
        self.data_manager.save_data(
            self.data_manager.TOURNAMENTS_FILE, self.tournaments_data
        )

        self.message_view.return_to_menu()

    def list_matches(self, selected_tournament):
        self.data_view.format_matches(selected_tournament)
        self.message_view.return_to_menu()

    def register_score(self, selected_tournament):
        if not self.data_view.format_matches(selected_tournament):
            return self.message_view.return_to_menu()

        current_round = selected_tournament["rounds"][-1]

        if current_round["scores_updated"] == True:
            self.message_view.generate_new_matches()
            return self.message_view.return_to_menu()

        self.matches_view.scoring(current_round["matches"])
        self.turn_manager.update_players_scores(selected_tournament)
        current_round["scores_updated"] = True

        current_round["end_date"] = self.turn(current_round["name"]).end_turn()

        self.data_manager.save_data(
            self.data_manager.TOURNAMENTS_FILE, self.tournaments_data
        )
        self.message_view.return_to_menu()
