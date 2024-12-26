from src.chess_tournament.models.element_manager import find_element_by_id


class TournamentSetupController:
    def __init__(
        self,
        tournament,
        turn,
        data_manager,
        turn_manager,
        data_view,
        tournament_view,
        message_view,
        matches_view,
    ):
        self.tournament = tournament
        self.turn = turn
        self.data_manager = data_manager
        self.turn_manager = turn_manager
        self.data_view = data_view
        self.tournament_view = tournament_view
        self.message_view = message_view
        self.matches_view = matches_view
        self.PLAYERS_FILE = "players.json"
        self.TOURNAMENTS_FILE = "tournaments.json"
        self.players_data = self.data_manager.load_data(self.PLAYERS_FILE)
        self.tournaments_data = self.data_manager.load_data(self.TOURNAMENTS_FILE)

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

                if any(
                    existing_player["id"] == player["id"]
                    for existing_player in selected_tournament["players"]
                ):
                    self.message_view.player_already_registered()
                else:
                    selected_tournament["players"].append(player)
                    self.message_view.new_entity_success("joueur")
            except (ValueError, TypeError):
                self.message_view.invalid_id()

        self.data_manager.save_data(self.TOURNAMENTS_FILE, self.tournaments_data)

    def list_tournament_players(self, selected_tournament):
        self.data_view.format_tournament_players(selected_tournament)
        self.message_view.return_to_menu()

    def generate_matches(self, selected_tournament):
        number_of_turns = selected_tournament["turn"]
        rounds = selected_tournament.setdefault("rounds", [])

        if len(rounds) >= number_of_turns:
            print("Tous les matchs sont déjà générés.")
            return self.message_view.return_to_menu()

        if rounds:
            scores = [match[0]["score"] for match in rounds[-1]["matches"]] + [
                match[1]["score"] for match in rounds[-1]["matches"]
            ]
            for score in scores:
                if score == 0:
                    print(
                        "\nVeuillez inscrire les scores des matchs du round en cours."
                    )
                    return self.message_view.return_to_menu()

        current_round_name = f"Round {len(rounds) + 1}"
        new_round = self.turn(current_round_name)

        players = selected_tournament["players"]

        if len(rounds) == 0:
            matches = self.turn_manager.shuffle(players)
        else:
            matches = self.turn_manager.sort_by_score(players)

        serialized_round = new_round.serialize()
        serialized_round["matches"] = matches
        rounds.append(serialized_round)

        self.data_view.format_matches(selected_tournament)

        self.data_manager.save_data(self.TOURNAMENTS_FILE, self.tournaments_data)
        self.message_view.return_to_menu()

    def list_matches(self, selected_tournament):
        self.data_view.format_matches(selected_tournament)
        self.message_view.return_to_menu()

    def register_score(self, selected_tournament):
        # variable for current round from generate_matches
        # update score for current_round
        # self.tournament_manager.update_player_score(selected_tournament, players)
        # new_turn.end_turn()
        pass
