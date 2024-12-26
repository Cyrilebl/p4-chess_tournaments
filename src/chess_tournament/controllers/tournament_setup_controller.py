from src.chess_tournament.models.element_manager import find_element_by_id


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
    ):
        self.tournament = tournament
        self.turn = turn
        self.data_manager = data_manager
        self.turn_manager = turn_manager
        self.data_view = data_view
        self.message_view = message_view
        self.tournament_view = tournament_view
        self.matches_view = matches_view
        self.players_data = self.data_manager.load_data(data_manager.PLAYERS_FILE)
        self.tournaments_data = self.data_manager.load_data(
            data_manager.TOURNAMENTS_FILE
        )

    def tournament_choice(self):
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
        self.data_view.format_players(self.players_data, "id")

        while True:
            try:
                user_choice = self.message_view.ask_player_id()
                if user_choice.lower() == "q":
                    break

                player = find_element_by_id(self.players_data, user_choice)
                selected_tournament.setdefault("players", [])
                # pop() birth_date
                if any(
                    existing_player["id"] == player["id"]
                    for existing_player in selected_tournament["players"]
                ):
                    self.message_view.player_already_registered()
                else:
                    player.pop("birth_date")
                    selected_tournament["players"].append(player)
                    self.message_view.new_entity_success("joueur")
            except (ValueError, TypeError):
                self.message_view.invalid_id()

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

        if rounds and self.turn_manager.check_scores(rounds[-1]["matches"]):
            self.message_view.record_scores()
            return self.message_view.return_to_menu()

        current_round_name = f"Round {len(rounds) + 1}"
        new_round = self.turn(current_round_name)

        if not rounds:
            matches = self.turn_manager.shuffle(selected_tournament)
        else:
            matches = self.turn_manager.sort_by_score(selected_tournament)

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
        matches_data = current_round["matches"]

        if not self.turn_manager.check_scores(matches_data):
            self.message_view.generate_new_matches()
            return self.message_view.return_to_menu()

        self.matches_view.scoring(matches_data)
        self.turn_manager.update_players_scores(selected_tournament)

        current_round["end_date"] = self.turn(current_round["name"]).end_turn()

        self.data_manager.save_data(
            self.data_manager.TOURNAMENTS_FILE, self.tournaments_data
        )
        self.message_view.return_to_menu()
