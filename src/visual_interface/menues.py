import datetime

def input_int_try_bucle(str_request):

    while True:
        print(str_request)
        try:
            #yatusabe


    

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
        print("introduce the day:")
        day = int(input())
        print("introduce the month:")
        month = input()
        print("introduce the year:")
        year = input()
        print("introduce the hour:")
        hour = input()
        print("introduce the minutes:")
        minute = input()
        try:
            output = datetime.datetime(year, month, day, hour, minute)
            if(output > actual_date):
                return output
            else:
                print("[ERROR] the date cannot be defore the actual date")
                print(f"actual date: [{actual_date}]")
        except Exception as e:
            print("the date was no valid because: ",e)
        
        




    