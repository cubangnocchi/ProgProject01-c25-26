from src.calendar.calendar import Calendar
from src.calendar.event_class.event import Event
from src.calendar.event_class.interval import interval
from src.inventory.inventory import Inventory
from src.inventory.human import Human
from src.inventory.item import Item
from src.manager import restrictions
from src.visual_interface import menues
 

def run():
    # main_calendar = something that loads everything 
    # main_inventory = something that loads the inventory
    #! remember to put an automatic empty calendar and inventory if there is none

    while True:
        menues.main_menue
        