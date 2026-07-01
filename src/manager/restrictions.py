from src.calendar.event_class.interval import interval
from src.calendar.event_class.event import Event
from src.inventory.item import Item
from src.inventory.human import Human
from src.calendar.calendar import Calendar
from src.inventory.inventory import Inventory
from src.manager import restrictions_data
from src.manager import data_search

# check all restrictions from here
def check_event(event: Event, calendar: Calendar, inventory: Inventory):
    
    #output
    error_list = []

    error_list = error_list + dependency_check(event, inventory)

    
    
    return error_list

# called from check_event, checks dependencies between event type, item types and crew specialities and status
def dependency_check(event: Event, inventory: Inventory):
    #output
    error_list = []

    #loading data from the event
    event_items = event.get_items_list(inventory)
    event_people = event.get_people_list(inventory)
    event_type = event.get_type()
    
    # ---------------- EVENT TYPE SECTION --------------
    #importing event_type related restrictions
    dep_event_type = restrictions_data.dependencies_event_type

    #dependency event_type - item_type
    dep_event_type_itemtype_list = dep_event_type["item_type"][event_type]    
    
    for item_type in dep_event_type_itemtype_list:
        if not(data_search.is_item_type_in_item_list(item_type, event_items)):
            error_str = ("an event of the type ¨"+ event_type + "¨ needs an item of the type ¨" + item_type + "¨")
            error_list.append(error_str)
    
    #dependency event_type - specialist
    dep_event_type_specialist_list = dep_event_type["specialist"][event_type]
    
    for speciality in dep_event_type_specialist_list:
        if not(data_search.is_specialist_in_people_list(speciality, event_people)):
            error_str = ("an event of the type ¨"+ event_type + "¨ needs a person specialized in ¨" + speciality + "¨")
            error_list.append(error_str)

    #dependency event_type - status
    dep_event_type_status_list = dep_event_type["status"][event_type]

    for status in dep_event_type_status_list:
        if not(data_search.is_status_in_people_list(status, event_people)):
            error_str = ("an event of the type ¨"+ event_type + "¨ needs an person with the status ¨" + status + "¨")
            error_list.append(error_str)
    return error_list

    # ---------------- EVENT PLACE SECTION --------------
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #! te quedaste por aquí ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    

# called from check_event, cheks exclusion criteria between event type, item types and crew specialities and status
def exclusion_check(event: Event, inventory: Inventory):
    #output
    error_list = []
    
    return error_list

# called from check_event, checks:
# - no person or unique item is in to places at the same time
# - the amount of a certain item used along all the events doesn't 
#   end with a negative mass paradox and sumons a warp drive...
def resources_n_crew_concistency(event: Event, calendar: Calendar, inventory: Inventory):
    #output
    error_list = []
    
    return error_list

# called from check_event, checks dependencies and exclusion restrictions
# related to the place of the event
def place_related_restrictions(event: Event, inventory: Inventory):
    #output
    error_list = []
    
    return error_list

# called from check_event, 
def dynamic_restrictions(event: Event, inventory: Inventory):
    #output
    error_list = []
    
    return error_list








