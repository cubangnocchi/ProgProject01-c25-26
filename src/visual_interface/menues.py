import datetime
import src.visual_interface.console_input_output as io
from src.calendar.event_class import event, interval 

  

def main_menue():

    options = ["1","2","3","4","5","x"] #add option keys here
    
    while open:
       print("}-------[Main Menue]--------{")
       print("press a [key] + [Enter↲] to select one of the following options:")
       print("[1] - list events")
       print("[2] - add event")
       print("[3] - add element to inventory")
       print("[4] - delete event")
       print("[5] - delete element from inventory")
       #.............
       print("[x] - exit")

       option_selected = input()
       if not (option_selected in options):
           print("wrong imput, try again")
           print(" ")
       else:
           print("option selected")
           return option_selected
       
def event_creation_menue(actual_date): 
    event_data = []
    print("")
    print("}-------[event creation menue]--------{")
    
    print("Introduce the name of the event")
    event_name = input()

    event_time = interval_creation_menue(actual_date)

    # implement item selection menue

    output = event.Event(event_name, event_time, [], [])

    return output
   

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
        day = io.input_int_bucle("introduce the day:")
        month = io.input_int_bucle("introduce the month:")
        year = io.input_int_bucle("introduce the year:")
        hour = io.input_int_bucle("introduce the hour:")
        minute = io.input_int_bucle("introduce the minutes:")
        try:
            output = datetime.datetime(year, month, day, hour, minute)
            if(output > actual_date):
                return output
            else:
                print("[ERROR] the date cannot be defore the actual date")
                print(f"actual date: [{actual_date}]")
        except Exception as e:
            print("the date was no valid because: ",e)
        
        




    