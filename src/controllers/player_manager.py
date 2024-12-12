import os
import json

class PlayerManager:
  def get_file_path(self, folder_path, file_name):
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)
    
    # Construct the full file path
    return os.path.join(folder_path, file_name)

  def load_data(self, folder_path, file_name):
    full_path = self.get_file_path(folder_path, file_name)
    
    if not os.path.exists(full_path):
      return None
    else:
      with open(full_path, "r") as file:
        return json.load(file)
      
  def save_to_json(self, folder_path, file_name, data):
    full_path = self.get_file_path(folder_path, file_name)

    existing_data = []
    existing_data.extend(data)
          
    with open(full_path, "w") as file:
      json.dump(existing_data, file, indent=4)
    