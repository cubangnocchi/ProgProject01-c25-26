from src.calendar.event_class.interval import interval
from src.calendar.event_class.event import Event
from src.inventory.item import Item
from src.calendar.calendar import Calendar
from src.inventory.inventory import Inventory


# check all restrictions from here
def check_event(event: Event, calendar: Calendar, inventory: Inventory):
    
    #output
    error_list = []

    
    return error_list

# called from check_event, checks dependencies between event type, item types and crew specialities and status
def dependency_check(event: Event, inventory: Inventory):

    #output
    error_list = []
    
    return error_list

# called from check_event, cheks exclusion criteria between event type, item types and crew specialities and status
def exclusion_check(event: Event, inventory: Inventory):
    #output
    error_list = []
    
    return error_list

def resources_n_crew_concistency(event: Event, calendar: Calendar, inventory: Inventory):
    #output
    error_list = []
    
    return error_list






