import datetime
from src.calendar.event_class import event
from src.calendar.event_class import interval

class Calendar:

    def __init__(self, places_names, initial_date):
        self.places = dict.fromkeys(places_names) # <----{this is not safe... try to change it}
        self.actual_date = initial_date

    
    def get_places (self):
        return self.places
    
    def get_event_list (self, place_key):
        return self.places(place_key)
    
    def get_actual_date(self):
        return self.actual_date
    
    def set_actual_date(self, new_date: datetime.datetime):
        self.actual_date = new_date

    def insert_event_in_place(self, new_event: event.Event, place_key):

        event_list = self.places(place_key)
        new_event_start_date = new_event.get_starting_date()

        if event_list == None:
            self.places(place_key).append(new_event)
        
        else:
            left, right = 0, len(event_list) - 1

            while(left < right):
                midle = (left + right)//2

                if(event_list(midle).get_starting_date() < new_event_start_date):
                    left = midle + 1
                else:
                    right = midle - 1

            new_event_pos = left
            
            self.places.insert(new_event_pos, new_event)
    