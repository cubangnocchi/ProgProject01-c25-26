from datetime import datetime
from src.calendar.event_class.event import Event
from src.calendar.event_class import interval

class Calendar:

    #-------<<<[constructor]>>>-------

    def __init__(self, event_list: list[Event], initial_date: datetime):
        self.event_list = event_list
        self.actual_date = initial_date

    #-------<<<[get parametrs]>>>-------

    def get_event_list(self) -> list[Event]:
        return self.event_list

    def get_actual_date(self) -> datetime:
        return self.actual_date
    
    
    #-------<<<[change parameters]>>>-------

    def insert_event_in_place(self, new_event: Event):
        
        new_event_start_date = new_event.get_starting_date()

        if self.event_list == None:
            self.event_list.append(new_event)
        
        else:
            self.event_list = Calendar.event_binary_insert(self.event_list, new_event)
    
    #-------<<<[json convertion methods]>>>-------

    def convert_to_dict(self):
        
        output = {
            "EVENTS": Calendar.event_list_to_dictionary(self.event_list),
            "INITIAL-DATE": self.actual_date.__str__()
        }
        
        return output
    
    @staticmethod
    def convert_dictionary_to_calendar(dictionary: dict):

        EVENTS_raw: dict[dict[str]] = dictionary["EVENTS"]
        
        EVENTS_processed = Calendar.dictionary_to_event_list(EVENTS_raw)
        

        output = Calendar(EVENTS_processed, datetime.strptime(dictionary["INITIAL-DATE"], '%Y-%m-%d %H:%M:%S'))

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
            print("the event is already in")
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