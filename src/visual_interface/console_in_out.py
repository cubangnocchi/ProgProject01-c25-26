from src.calendar.event_class.event import Event
from src.inventory.item import Item
from src.inventory.human import Human
from datetime import datetime

def input_positive_int_bucle(str_request):
    while True:
        print(str_request)
        try: 
            output = int(input())
            if(output > 0):
                return output
            else:
                print("Input was no valid because it most be a positive number")
        except Exception as e:
            print("Input was no valid because: ",e)


def input_int_bucle(str_request: str):

    while True:
        print(str_request)
        try: 
            output = int(input())
            return output
        except Exception as e:
            print("Input was no valid because: ",e)

def input_int_inrange_bucle(str_request: str, 
                            maxvalue: int, 
                            minvalue: int):
    
    while True:
        print(str_request)
        try: 
            output = int(input())
            if((minvalue <= output) and 
               (output <= maxvalue)):
                return output
            else:
                print(f"Input out of range: {minvalue} < input < {maxvalue}")
        except Exception as e:
            print("Input was no valid because: ",e)

def multiple_input_int_bucle(str_request_list):
    output = []

    for str in str_request_list:
        output.append(input_int_bucle(str))

    return output

def print_item_list(item_dict: dict[str , Item]):

    print(" ")
    
    key_list = list(item_dict.keys())

    for key in key_list:
        print(f"item name: {item_dict[key].get_name()}")
        print(f"      key: {key}")
        print(f"     type: {item_dict[key].get_type()}")
        if(item_dict[key].have_amount()):
            print(f"   amount: {item_dict[key].get_amount()}")
        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")



def print_event_list(event_list: list[Event]):
    
    print(" ")
    for event in event_list:
        print(f"event name: {event.get_name()}")
        print(f" |- time: {event.get_starting_date()} - {event.get_ending_date()}")
        print(f" |- amount of people: {len(event.get_people_keys())}")
        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

def error_output(error):
    print(error)

def print_item_dict(event_dict: dict[str, Item]):

    key_list = list(event_dict.keys())

    for key in key_list:
        item_i = event_dict[key]
        print(f"{key} - name: {item_i.get_name()}")
        print(f" |- type {item_i.get_type()}")
        amount = item_i.get_amount()
        if(amount != -1):
            print(f" |- amount: {amount}")
        else:
            print(f" |- amounnt: unique")
        print("")

def print_people_dict(people_dict: dict[str, Human], actual_date: datetime):
    
    key_list = list(people_dict.keys())

    for key in key_list:
        human_i = people_dict[key]
        print(f"{key} - name: {human_i.get_name()}")
        print(f" |- age: {human_i.get_age(actual_date)}")
        print(f" |- speciality: {human_i.get_speciality}")
        print(f" |- status: {human_i.get_status}")
        print("")