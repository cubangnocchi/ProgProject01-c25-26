from src.calendar.event_class.interval import interval
from src.calendar.event_class.event import Event
from src.visual_interface import menues
import datetime



def test_intervals():

    f1 = datetime.datetime(2200, 10, 10)
    f2 = datetime.datetime(2250, 10, 10)
    f3 = datetime.datetime(2240, 10, 10)
    f4 = datetime.datetime(2270, 10, 10)

    a = interval(f1,f2)
    
    b = interval(f3,f4)
    
    print("patata")
    
    print(interval.is_it_overlaping(a, b))
    print(interval.is_it_overlaping(b, a))

def test_event():
    print("testing events")

    
    f1 = datetime.datetime(2200, 10, 10)
    f2 = datetime.datetime(2250, 10, 10)

    evento01 = Event("patata", f1, f2, "01")

    print(evento01.get_ending_date())

def date_creation_test():
    
    actual_date = datetime.datetime(2026,2,3,14,46)
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(menues.date_cration_menue(actual_date))
    
       