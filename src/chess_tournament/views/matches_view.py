class MatchesView:
    def scoring(self, matches_data):
        for i, match in enumerate(matches_data):
            first_player, second_player = match

            while True:
                result = input(
                    f"\nQuel joueur a gagné le match {i + 1} ? (1 pour {first_player['first_name']}, "
                    f"2 pour {second_player['first_name']}, 3 pour égalité): "
                )
                match result:
                    case "1":
                        first_player["score"] += 1
                        break
                    case "2":
                        second_player["score"] += 1
                        break
                    case "3":
                        first_player["score"] += 0.5
                        second_player["score"] += 0.5
                        break
                    case _:
                        print("Choix invalide, veuillez entrer 1, 2, ou 3.")

        print("\nResultats du tour:")
        for match in matches_data:
            first_player, second_player = match
            print(
                f"{first_player['last_name']} {first_player['first_name']} : {first_player['score']}"
            )
            print(
                f"{second_player['last_name']} {second_player['first_name']} : {second_player['score']}"
            )
