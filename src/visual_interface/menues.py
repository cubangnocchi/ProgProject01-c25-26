import datetime

from src.visual_interface import console_in_out
from src.visual_interface.menue import SelectionMenue

from src.calendar.event_class import event, interval 
from src.inventory import inventory, human, item

def main_menue():
    
    mainmenue = SelectionMenue(
        "MAIN MENUE",
        {
            "1": "list events",
            "2": "list items",
            "3": "list crew",
            "4": "create event",
            "5": "delete event",
            "6": "add item",
            "7": "delete item",
            "8": "add crew member",
            "9": "leave crew member",
            "x": "exit"
        },
        "press a [key] + [Enter↲] to select one of the options:"
    )

    return mainmenue.print()


def event_creation_menue(actual_date): 
    event_data = []
    print("")
    print("}-------[event creation menue]--------{")
    
    print("Introduce the name of the event")
    event_name = input()

    event_time = interval_creation_menue(actual_date)

    output = event.Event(event_name, event_time, [], [])

    return output
#! =================================================================================
def inventory_selection_menue(available_from_inventory: inventory.Inventory):
    output_items = 0
    output_people = people_selection_menue(available_from_inventory.get_people)

def people_selection_menue(people_list):
    print("implementando")

#! =================================================================================

def interval_creation_menue(actual_date):
    
    print("### introduce the starting time")
    starting_date = date_cration_menue(actual_date)
    print("### introduce the ending time")
    while True:
        ending_date = date_cration_menue(actual_date)
        if(starting_date < ending_date):
            return interval.interval(starting_date, ending_date)
        else:
            print("[ERROR] the ending time cannot be before starting time, time travel is not implemented")
            print(f"actual date: [{starting_date}]")
        

def date_cration_menue(actual_date):
    while True:
        print("}-------[date creation menue]--------{")
        day = console_in_out.input_int_bucle("introduce the day:")
        month = console_in_out.input_int_bucle("introduce the month:")
        year = console_in_out.input_int_bucle("introduce the year:")
        hour = console_in_out.input_int_bucle("introduce the hour:")
        minute = console_in_out.input_int_bucle("introduce the minutes:")
        try:
            output = datetime.datetime(year, month, day, hour, minute)
            if(output > actual_date):
                return output
            else:
                print("[ERROR] the date cannot be defore the actual date")
                print(f"actual date: [{actual_date}]")
        except Exception as e:
            print("the date was no valid because: ",e)
        
        




    