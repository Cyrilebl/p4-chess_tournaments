import os
import json

# Players data are on players.json file
def save_to_json(folder_path, file_name, data):
  
  # Ensure the folder exists
  os.makedirs(folder_path, exist_ok=True)
  
  # Construct the full file path
  full_path = os.path.join(folder_path, file_name)
  
  if os.path.exists(full_path):
    with open(full_path, "r") as file:
      existing_data = json.load(file)
  else:
    existing_data = []
  
  existing_data.extend(data)
        
  with open(full_path, "w") as file:
    json.dump(existing_data, file, indent=4)