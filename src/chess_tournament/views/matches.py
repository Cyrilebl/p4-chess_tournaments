class Matches:
    def scoring(self, first_player, second_player):
        while True:
            result = input(
                f"Quel joueur a gagné ce match ? (1 pour {first_player['first_name']}, 2 pour {second_player['first_name']}, 3 pour égalité): "
            )
            if result == "1":
                first_player["score"] += 1
                break
            elif result == "2":
                second_player["score"] += 1
                break
            elif result == "3":
                first_player["score"] += 0.5
                second_player["score"] += 0.5
                break
            else:
                print("Choix invalide, veuillez entrer 1, 2, ou 3.")

    def display_turn_matches(self, turn):
        for i, match in enumerate(turn.matches, 1):
            print(f"\nMatch {i}:")
            self.scoring(match[0][0], match[1][0])

        print("\nResultats du tour:")
        for match in turn.matches:
            pass