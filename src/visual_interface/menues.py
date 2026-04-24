from datetime import datetime

from src.visual_interface import console_in_out
from src.visual_interface.selection_menue import SelectionMenue

from src.calendar.event_class import event, interval 
from src.inventory import inventory, human, item

def main_menue():
    
    mainmenue = SelectionMenue(
        "MAIN MENUE",
        {
           #" ": " ",
            "1": "list events",
            "2": "list items ",
            "3": "list crew",
            "4": "add item to inventoory",
            "5": "create event",
            "6": "add crew member",
            "x": "exit"
        },
        "press a [key] + [Enter↲] to select one of the options:"
    )

    return mainmenue.print_get_key()

def item_list_menue(item_dict: dict[str ,item.Item]):
    
    if(item_dict == {} or item_dict == None):
        print(" ")
        print("There are no items to list")
    else:
        console_in_out.print_item_list(item_dict)

def item_creation_menue():
    print("----[item addition menue]----")
    print("introduce the item name: ")
    name = input()
    
    num_dict_of_types = SelectionMenue.create_numerable_dict_from_list(item.Item.item_type_list())
    select_type_menue = SelectionMenue(
        "select the type of the item",
        num_dict_of_types,
        "press a [key] + [Enter↲] to select one of the options:"
    )
    item_type = select_type_menue.print_get_option()
    
    #! ahora implemento select
    # print("introduce the type: ")
    # item_type = input()
    
    expendable_menue = SelectionMenue( #this is clearly completly unnecesary
        "Is it expendable?",
        {
            "1": "yes",
            "0": "no"
        },
        "press a [key] + [Enter↲] to select one of the options:"
    )
    exp_mn_in = expendable_menue.print_get_key()
    if(exp_mn_in == "1"):
        expendable = True
    if(exp_mn_in == "0"):
        expendable = False

    new_item = item.Item(name, item_type, expendable)

    amount_menue = SelectionMenue( #this is clearly completly unnecesary
        "Is it unique or it has an amount?",
        {
            "1": "it has an amounnt",
            "0": "it is unique"
        },
        "press a [key] + [Enter↲] to select one of the options:"
    )
    amount_menue_input = amount_menue.print_get_key()

    if(amount_menue_input == "1"):
        amount = console_in_out.input_positive_int_bucle("introduce the amount of the item:")
        new_item.set_amount(amount)

    return new_item    

def event_listing_menue(places: dict[str, list[event.Event]]):
    
    mode_menue = SelectionMenue(
        "Select how to list the events",
        {
            "1": "select from place",
            "2": "list all",
            "x": "go back"
        },
        "press a [key] + [Enter↲] to select one of the options:"
    )
    mode = mode_menue.print_get_key()

    if(mode == "x"):
        return
    if(mode == "1"):

        places_names_list = list(places.keys())
        
        places_names_list_dict = SelectionMenue.create_numerable_dict_from_list(places_names_list)
        event_place_menue = SelectionMenue("Select a Place",
                                           places_names_list_dict,
                                           "introduce a number and press [Enter↲] to select one of the options:")
        selected_place = event_place_menue.print_get_option()
        if(places[selected_place] == [] or places[selected_place] == None):
            print(f"no events were asigned to the place: {selected_place}")
            print(" - - - - - - - - - - - - - - - - - -")
            return
        
        console_in_out.print_event_list(places[selected_place])
        return

    elif(mode == "2"):
        print("NOT IMPLEMENTED") #!implement it!!!!!!!!!!!!!  



def event_creation_menue(actual_date: datetime, places_names_list: dict[str]): 
    event_data = []
    print("")
    print("}-------[event creation menue]--------{")
    
    print("Introduce the name of the event")
    event_name = input()

    event_time = interval_creation_menue(actual_date)
    
    places_names_list_dict = SelectionMenue.create_numerable_dict_from_list(places_names_list)
    event_place_menue = SelectionMenue("Select a Place",
                                 places_names_list_dict,
                                 "introduce a number and press [Enter↲] to select one of the options:")
    event_place = event_place_menue.print_get_option()

    output = (event.Event(event_name, event_time, [], []), event_place)

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
            output = datetime(year, month, day, hour, minute)
            if(output > actual_date):
                return output
            else:
                print("[ERROR] the date cannot be defore the actual date")
                print(f"actual date: [{actual_date}]")
        except Exception as e:
            print("the date was no valid because: ",e)
        
        




    