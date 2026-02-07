import datetime

def input_int_try_bucle(str_request):

    while True:
        print(str_request)
        try: 
            output = int(input())
            return output
        except Exception as e:
            print("Input was no valid because: ",e)
            


    

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
       
def error_output(error):
    print(error)

def event_creation_menue():
    event_data = []
    print("")
    print("}-------[event creation menue]--------{")
    #name

    #date

def date_cration_menue(actual_date):
    while True:
        print("}-------[date creation menue]--------{")
        day = input_int_try_bucle("introduce the day:")
        month = input_int_try_bucle("introduce the month:")
        year = input_int_try_bucle("introduce the year:")
        hour = input_int_try_bucle("introduce the hour:")
        minute = input_int_try_bucle("introduce the minutes:")
        try:
            output = datetime.datetime(year, month, day, hour, minute)
            if(output > actual_date):
                return output
            else:
                print("[ERROR] the date cannot be defore the actual date")
                print(f"actual date: [{actual_date}]")
        except Exception as e:
            print("the date was no valid because: ",e)
        
        




    