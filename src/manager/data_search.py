from src.calendar.event_class.interval import interval
from src.calendar.event_class.event import Event
from src.inventory.item import Item
from src.inventory.human import Human
from src.calendar.calendar import Calendar
from src.inventory.inventory import Inventory

def is_item_type_in_item_list(item_type: str, item_list: list[Item]):

    for item in item_list:
        if(item.get_type() == item_type):
            return True
        
    return False

def is_specialist_in_people_list(speciality: str, people_list: list[Human]):
    
    for human in people_list:
        if(human.get_speciality() == speciality):
            return True
        
    return False

def is_status_in_people_list(status: str, people_list: list[Human]):

    for human in people_list:
        if(human.get_status() == status):
            return True
        
    return False


