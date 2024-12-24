import os
import json


class DataManager:
    def __init__(self, folder_path="src/data"):
        self.folder_path = folder_path

    def get_file_path(self, file_name):
        # Ensure the folder exists
        os.makedirs(self.folder_path, exist_ok=True)

        # Construct the full file path
        return os.path.join(self.folder_path, file_name)

    def load_data(self, file_name):
        full_path = self.get_file_path(file_name)
        if not os.path.exists(full_path):
            return []
        else:
            with open(full_path, "r") as file:
                return json.load(file)

    def save_data(self, file_name, data):
        full_path = self.get_file_path(file_name)
        with open(full_path, "w") as file:
            json.dump(data, file, indent=4)

    def generate_new_id(self, data):
        existing_ids = [item["id"] for item in data]
        return max(existing_ids, default=0) + 1
