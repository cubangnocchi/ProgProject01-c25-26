from resources.calendar.event_class import interval
import datetime


def test_intervals():

    f1 = datetime.datetime(2200, 10, 10)
    f2 = datetime.datetime(2200, 10, 10)
    f3 = datetime.datetime(2200, 10, 10)
    f4 = datetime.datetime(2200, 10, 10)

    a = interval(f1,f2)
    
    b = interval(f3,f4)
    
    print("patata")
    print(interval.is_it_overlaping(a, b))