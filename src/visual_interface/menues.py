from datetime import datetime

from src.visual_interface import console_in_out
from src.visual_interface.selection_menue import SelectionMenue

from src.calendar.event_class import event, interval 
from src.calendar.calendar import Calendar
from src.inventory.inventory import Inventory
from src.inventory import inventory, human, item

def main_menue() -> str:
    
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
            "x": "exit",
        },
        "press a [key] + [Enter↲] to select one of the options:"
    )

    return mainmenue.print_get_key()
    
def item_list_menue(item_dict: dict[str ,item.Item]):
    
    if(item_dict == {} or item_dict == None):
        print(" ")
        print("There are no items to list")
    else:
        console_in_out.print_item_dict(item_dict)

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
    
    #! ahora toddo esto no work ............................
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

def event_creation_menue(calendar: Calendar, inventory: Inventory):

    print("")
    print("}-------[event creation menue]--------{")
    
    print("Introduce the name of the event")
    event_name = input()

    event_time = interval_creation_menue(calendar.get_actual_date())
    
    places_names_list_dict = SelectionMenue.create_numerable_dict_from_list(inventory.get_places_list())
    event_place_menue = SelectionMenue("Select a Place",
                                 places_names_list_dict,
                                 "introduce a number and press [Enter↲] to select one of the options:")
    event_place = event_place_menue.print_get_option()

    num_dict_event_types = SelectionMenue.create_numerable_dict_from_list(event.Event.get_event_type_list())
    event_type_menue = SelectionMenue(
        "select the type of event",
        num_dict_event_types,
        "introduce a number and press [Enter↲] to select one of the options:"
    )
    event_type = event_type_menue.print_get_option()

    #item asignation: item selection menue

    output = (event.Event(event_name,
                          event_time,
                          [], 
                          [], 
                          [],
                          event_type,
                          event_place))

    return output
    
#!-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-++--+--++
#! =================================================================================

def items_selection_menue(items: dict[str, item.Item]):
    
    print("[ITEM SELECTION MENUE]")
    console_in_out.print_item_dict(items)

    menueble_dict_items = SelectionMenue.item_dict_to_menueable_dict(items)
    select_item_menue = SelectionMenue(
        "item_selection_menue",
        menueble_dict_items,
        "select"
    )
    output = select_item_menue.get_key()
    
    #! FALTA el amount... e facil
    return output
    
def items_selection_menue_bucle(items: dict[str, item.Item]):
    output = []
    while(True):
        key_and_amount = items_selection_menue(items)
        output.append(key_and_amount)
        more_or_exit_menue = SelectionMenue(
            "Do you want to...",
            {
                "1": "add one more item?",
                "x": "end the item selection?"
            },
            "introduce a key and press [Enter↲] to select one of the options:"
        )
        selection = more_or_exit_menue.print_get_key()
        if(selection == "x"):
            break

    return output
    # output_people = people_selection_menue(available_from_inventory.get_people)

def people_creation_menue(actual_date): #!add actual date pa que la fecha de nacimiento no de bateo

    print("New crew memeber aboard e7")
    print("pleace introduce his/her/something name")
    name = input()
 
    num_dict_speciality = SelectionMenue.create_numerable_dict_from_list(human.Human.get_specialization_list())
    speciality_menue = SelectionMenue(
        "select the speciality",
        num_dict_speciality,
        "introduce a number and press [Enter↲] to select one of the options:"
    )
    speciality = speciality_menue.print_get_option()

    num_dict_status = SelectionMenue.create_numerable_dict_from_list(human.Human.get_status_list())
    status_menue = SelectionMenue(
        "select the status",
        num_dict_status,
        "introduce a number and press [Enter↲] to select one of the options:"
    )
    status = status_menue.print_get_option()
    
    print("Introduce the birthdate")
    day_born = birthdate_creation_menue(actual_date) #!pon una restricción en plan que no haya nacido mañana
    
    output = human.Human(name,
                         speciality,
                         status,
                         day_born
                         )
    
    return output

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

def birthdate_creation_menue(actual_date):
    while True:
        print("}-------[date creation menue]--------{")
        day = console_in_out.input_int_bucle("introduce the day:")
        month = console_in_out.input_int_bucle("introduce the month:")
        year = console_in_out.input_int_bucle("introduce the year:")
        try:
            output = datetime(year, month, day)
            if(output < actual_date):
                return output
            else:
                print("[ERROR] the date cannot be after the actual date")
                print(f"actual date: [{actual_date}]")
        except Exception as e:
            print("the date was no valid because: ",e)
            