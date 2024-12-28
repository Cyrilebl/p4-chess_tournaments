class Helpers:
    def find_element_by_id(self, user_choice, elements_data):
        try:
            user_id = int(user_choice)
        except ValueError:
            print(f"'{user_choice}' n'est pas un ID valide.")
            return None

        element = next(
            (element for element in elements_data if element["id"] == user_id),
            None,
        )

        if element is None:
            print(f"'Aucun élément trouvé avec l'ID {user_choice}'")
        return element
