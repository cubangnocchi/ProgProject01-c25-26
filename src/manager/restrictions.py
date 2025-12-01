from src.calendar.event_class.interval import interval
from src.calendar.event_class.event import Event
from src.inventory.item import Item

# -------------[Time restriction methods]---------------------------------------------------------------------------
def global_time_consistency_check (actual_time, events_list):

    if(not valid_from_actual_time(actual_time, events_list[0])):
        return False
    
    for event_a in events_list:
        if(time_consistency_check(event_a, events_list)):
            return False
            
    return True

def time_consistency_check (event, events_list):

    for event_a in events_list:
        if(interval.is_it_overlaping(event_a.get_interval(), event.get_interval())):
            return False
            
    return True

def valid_from_actual_time(actual_time, event):
    
    if(event.get_sarting_date() < actual_time):
        return False
        
    return True


# ------------[Inventory consistency methods]

# key coincidences

