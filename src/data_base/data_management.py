import json
import os
from src.calendar.calendar import Calendar
from src.inventory.inventory import Inventory

def load_data(FILEPATH):

    if not os.path.exists(FILEPATH):
        print("[no data base was found]")
        return {}
    
    try:
        with open(FILEPATH, 'r') as f:
            data = json.load(f)
            return data
    except Exception:
        print(f"Error loading the data base: {Exception}")

def convert_json_to_objects(data):
    
    return 

def convert_objects_to_json(calendar: Calendar, inventory: Inventory, metadata):
    output = {}

    return output

def save_data(FILEPATH, data):
    with open(FILEPATH, 'w') as f:
        json.dump(data, f, indent=4)

