from ..calendar.calendar import Calendar
from ..calendar.event_class.event import Event
from ..calendar.event_class.interval import interval
from ..inventory.inventory import Inventory
from ..inventory.human import Human
from ..inventory.item import Item
from . import restrictions
from ..visual_interface import menues
from src.visual_interface import console_input_output as io
import datetime 

def run():
    # main_calendar = something that loads everything 
    # main_inventory = something that loads the inventory
    actual_date = datetime.datetime(2026,2,3,14,46)
    #! remember to put an automatic empty calendar and inventory if there is none

    while True:
        option_selected = menues.main_menue()

        if(option_selected == "x"):
            #save all()
            break

        #if(option_selected == 1):
            #lista

        if(option_selected == "2"):
            add_event()        
        
        else:
            io.error_output("something went wrong, perhabs the function is not implemented")

def add_event():
    event_data = menues.event_creation_menue()

    #algo que recorra la data pa crear una instancia de evento y 
    #guardarla en la variable local

    