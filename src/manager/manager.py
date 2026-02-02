from ..calendar.calendar import Calendar
from ..calendar.event_class.event import Event
from ..calendar.event_class.interval import interval
from ..inventory.inventory import Inventory
from ..inventory.human import Human
from ..inventory.item import Item
from . import restrictions
from ..visual_interface import menues
 

def run():
    # main_calendar = something that loads everything 
    # main_inventory = something that loads the inventory
    #! remember to put an automatic empty calendar and inventory if there is none

    # while True:
    menues.main_menue()
        