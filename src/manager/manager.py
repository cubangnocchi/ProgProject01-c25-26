from src.calendar.calendar import Calendar 
from src.calendar.event_class.event import Event
from src.calendar.event_class.interval import interval
from src.inventory.inventory import Inventory
from src.inventory.human import Human
from src.inventory.item import Item
#from . import restrictions
from src.visual_interface import menues
from src.visual_interface import console_in_out as io
from src.data_base import data_management
from datetime import datetime 

#global variables
FILEPATH = 'src/data_base/save01.json'
    
raw_data = data_management.load_data(FILEPATH)
data = data_management.convert_json_to_objects(raw_data)
main_calendar = data[0]
main_inventory = data[1]


def run():

    main_bucle()

    save_data()

def save_data():
    save = data_management.convert_objects_to_json(main_calendar, main_inventory)
    data_management.save_data(FILEPATH, save)

def main_bucle():
    
    while True:
        option_selected = menues.main_menue()

        if(option_selected == "x"):
            break

        if(option_selected == "1"):
            list_events()

        if(option_selected == "2"):
            list_items()

        if(option_selected == "4"):
            add_item()

        if(option_selected == "5"):
            add_event()   

        if(option_selected == "6"):
            add_crew_member()     
        
def add_item():
    main_inventory.add_item(menues.item_creation_menue())
    save_data()

def add_event():
    event_data = menues.event_creation_menue(main_calendar, 
                                             main_inventory)

    main_calendar.insert_event_in_place(event_data)
    save_data()

def add_crew_member():
    main_inventory.add_human(menues.people_creation_menue(main_calendar.get_actual_date()))
    save_data()
    
def list_events():
    menues.event_listing_menue(main_calendar.get_places_with_events())
    #aquí agregas opciones para modificar cosas

def list_items():

    menues.item_list_menue(main_inventory.get_items())
    #aquí agregas opciones para modificar cosa



    #algo que recorra la data pa crear una instancia de evento y 
    #guardarla en la variable local

    