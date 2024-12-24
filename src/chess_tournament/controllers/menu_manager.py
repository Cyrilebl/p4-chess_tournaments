class MenuManager:
    def handle_tournament_management(self, user_choice, id):
        selected_tournament = next(
            tournament for tournament in self.tournaments_data if tournament["id"] == id
        )

        match user_choice:
            case 1:
                # Ajouter des joueurs au tournoi
                print(self.player_manager.list_player_by_id())
                while True:
                    # Sélectionner un joueur
                    new_player_id = input(
                        "Entrez l'ID du joueur à ajouter (ou 'q' pour quitter): "
                    )

                    if new_player_id.lower() == "q":
                        break

                    try:
                        # Trouver le joueur correspondant
                        player = next(
                            (
                                p
                                for p in self.players_data
                                if p["id"] == int(new_player_id)
                            ),
                            None,
                        )
                    except ValueError:
                        print("Veuillez entrer un ID valide.")
                        continue

                    if not player:
                        print("Joueur introuvable. Veuillez réessayer.")
                        continue

                    # Ajouter le joueur au tournoi
                    if "players" not in selected_tournament:
                        selected_tournament["players"] = []

                    # Empêcher les doublons
                    if not any(
                        existing_player["id"] == player["id"]
                        for existing_player in selected_tournament["players"]
                    ):
                        selected_tournament["players"].append(player)
                        player["score"] = 0
                        print(
                            f"{player['first_name']} {player['last_name']} a été ajouté au tournoi."
                        )
                    else:
                        print("Ce joueur fait déjà partie du tournoi.")

                self.data_manager.save_data(self.TOURNAMENT_FILE, self.tournaments_data)
                return "Ajout de joueurs terminé."

            case 2:
                try:
                    players_data = selected_tournament["players"]
                    return self.data_display.format_tournament_players(players_data)
                except KeyError:
                    return "Aucun joueur dans ce tournoi."

            case 3:
                # Générer les matchs
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
                        create_turn = self.tournament_manager.shuffle(
                            f"Round {i}", players
                        )
                    else:
                        create_turn = self.tournament_manager.sort_by_score(
                            f"Round {i}", players
                        )

                    print(create_turn)
                    self.match_results.display_turn_matches(create_turn)
                    create_turn.end_turn()
                    selected_tournament["matches"].append(create_turn.to_dict())

                    self.tournament_manager.update_player_score(
                        selected_tournament, players
                    )
                    self.data_manager.save_data(
                        self.TOURNAMENT_FILE, self.tournaments_data
                    )

                return "Match terminés."

            case 4:
                return "Match affichés."

            case 5:
                return self.menu.tournaments_menu()
