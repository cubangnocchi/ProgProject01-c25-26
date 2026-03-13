import json
import os
from datetime import datetime
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

    try:
        output = (Calendar.convert_dictionary_to_calendar(data["CALENDAR"]),
                  Inventory.convert_dict_to_inventory(data["INVENTORY"]))
        print("debug, load worked")
        return output
    except:
        return defoult_empty_data()
    
def defoult_empty_data():
    defoult_places = {
        "Control Bridge" : [],
        "Crew Quarters"  : [],
        "Fusion Reactor" : [],
        "Mining Bay"     : [],
        "Cargo Bay"      : [],
        "Laboratory"     : [],
        "Services Room"  : [],
        "Data Center"    : [],
        "Ship Exterior"  : [],
    }
    defoult_starting_date = datetime(2350, 1, 1)

    empty_calendar = Calendar(defoult_places, defoult_starting_date)

    empty_inventory = Inventory({}, {}, 0)

    output = (empty_calendar, empty_inventory)

    return output

def convert_objects_to_json(calendar: Calendar, inventory: Inventory):
    output = {}

    output["CALENDAR"] = calendar.convert_to_dict()
    output["INVENTORY"] = inventory.convert_to_dict() 

    return output

def save_data(FILEPATH, data):
    with open(FILEPATH, 'w') as f:
        json.dump(data, f, indent=4)

