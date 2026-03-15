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

    save = data_management.convert_objects_to_json(main_calendar, main_inventory)
    data_management.save_data(FILEPATH, save)

def main_bucle():
    
    while True:
        option_selected = menues.main_menue()

        if(option_selected == "x"):
            break

        #if(option_selected == 1):
            #lista

        if(option_selected == "2"):
            add_event()        
        
        else:
            io.error_output("something went wrong, perhabs the function is not implemented")

def add_event():
    event_data: tuple[Event, str] = menues.event_creation_menue(main_calendar.get_actual_date(), 
                                                                main_calendar.get_places_names())

    main_calendar.insert_event_in_place(event_data)


    #algo que recorra la data pa crear una instancia de evento y 
    #guardarla en la variable local

    