from src.calendar.event_class.event import Event
from datetime import datetime

def input_int_bucle(str_request):

    while True:
        print(str_request)
        try: 
            output = int(input())
            return output
        except Exception as e:
            print("Input was no valid because: ",e)

def multiple_input_int_bucle(str_request_list):
    output = []

    for str in str_request_list:
        output.append(input_int_bucle(str))

    return output

def print_event_list(event_list: list[Event]):
    
    print(" ")
    for event in event_list:
        print(f"event name: {event.get_name()}")
        print(f" |- time: {event.get_starting_date()} - {event.get_ending_date}")
        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

def print_event_and_place_list(event_list: list[Event, str]):
    
    print(" ")
    for selected in event_list:
        event = selected[0]
        place = selected[1]
        print(f"place: {place} event name: {event.get_name()}")
        print(f" |- time: {event.get_starting_date()} - {event.get_ending_date}")
        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

def error_output(error):
    print(error)

