from datetime import datetime
from src.calendar.event_class.event import Event
from src.calendar.event_class import interval

class Calendar:

    #-------<<<[constructor]>>>-------

    def __init__(self, places: dict[str, list[Event]], initial_date: datetime):
        self.places = places
        self.actual_date = initial_date

    #-------<<<[get parametrs]>>>-------

    def get_places (self):
        return self.places
    
    def get_event_list_from_place (self, place_key):
        return self.places(place_key)
    
    #-------<<<[change parameters]>>>-------

    def insert_event_in_place(self, new_event: Event, place_key: str):

        event_list = self.places[place_key]
        new_event_start_date = new_event.get_starting_date()

        if event_list == None:
            self.places[place_key].append(new_event)
        
        else:
            self.places[place_key] = Calendar.event_binary_insert(self.places[place_key], new_event)
    
    #-------<<<[json convertion methods]>>>-------

    def convert_to_dict(self):
        
        output = {
            "PLACES": {},
            "INITIAL-DATE": self.actual_date.__str__()
        }
        
        dic_places = {}
        places_names_list = list(self.places.keys())

        for place_name in places_names_list:
            dic_places[place_name] = Calendar.event_list_to_dictionary(self.places[place_name])

        output["PLACES"] = dic_places

        return output
    
    @staticmethod
    def convert_dictionary_to_calendar(dictionary: dict):

        PLACES_raw = dictionary["PLACES"]
        
        places_names_list = list(PLACES_raw.keys())
        PLACES_processed = {}

        for place_name in places_names_list:
            PLACES_processed[place_name] = Calendar.dictionary_to_event_list(PLACES_raw[place_name])
        

        output = Calendar(PLACES_processed, dictionary["INITIAL-DATE"])

        return output

    #-------<<<[internal methods]>>>-------
    
    @staticmethod
    def dictionary_to_event_list(event_dictionary):
        i = 0
        output_list = []
        while (i < len(event_dictionary)):
            output_list.append(Event.dictionary_to_event(event_dictionary[str(i)]))
            i += 1
    
        return output_list

    @staticmethod
    def event_list_to_dictionary(event_list: list[Event]):
        output_dictionary = {}
        i = 0
        for element in event_list:
            output_dictionary[i] = element.get_as_dictionary()
            i += 1

        return output_dictionary

    @staticmethod
    def event_binary_insert(event_list: list[Event], to_insert: Event):

        if(event_list == []): #in case it is empty
            return [to_insert]
    
        if(to_insert in event_list):
            print("the number is already in")
            return event_list
        
        left = 0
        right = len(event_list) - 1
        index = len(event_list)

        while left <= right:
            midle = (left + right)//2
            if to_insert.get_starting_date() < event_list[midle].get_starting_date():
                index = midle
                right = midle - 1
            else:
                left = midle + 1
    
        if(index == len(event_list)):
            event_list.append(to_insert)
        else:
            event_list.insert(index, to_insert)

        return event_list
    
#! create methods for format change 