class InformativeMessage:
    def quit_program(self):
        print("\nÀ bientôt !")

    def new_entity_success(self, entity_name):
        print(f"\nLe {entity_name} a été ajouté avec succès.")

    def no_current_data(self, data):
        if data is None:
            print(f"\nAucune donnée.")

    def return_to_menu(self):
        input("\nAppuyez sur Entrée pour revenir au menu...")
