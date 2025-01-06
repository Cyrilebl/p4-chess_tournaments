class MatchesView:
    def scoring(self, matches_data, players_data, selected_tournament):
        tournament_players_dict = {
            player["id"]: player for player in selected_tournament["players"]
        }
        players_dict = {player["id"]: player for player in players_data}

        matches_data = [match for match in matches_data if match[0][1] != -1]

        for i, match in enumerate(matches_data):
            first_player_id, second_player_id = match[0]
            player_score = match[1]

            first_player = players_dict.get(first_player_id)
            second_player = players_dict.get(second_player_id)

            tournament_first_player = tournament_players_dict.get(first_player_id)
            tournament_second_player = tournament_players_dict.get(second_player_id)

            while True:
                result = input(
                    f"\nQuel joueur a gagné le match {i + 1} ? "
                    f"(1 pour {first_player['first_name']}, "
                    f"2 pour {second_player['first_name']}, 3 pour égalité): "
                )
                match result:
                    case "1":
                        player_score[0] += 1
                        tournament_first_player["score"] += 1
                        break
                    case "2":
                        player_score[1] += 1
                        tournament_second_player["score"] += 1
                        break
                    case "3":
                        player_score[0] += 0.5
                        player_score[1] += 0.5
                        tournament_first_player["score"] += 0.5
                        tournament_second_player["score"] += 0.5
                        break
                    case _:
                        print("Choix invalide, veuillez entrer 1, 2, ou 3.")
