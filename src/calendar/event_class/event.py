import datetime
from src.calendar.event_class.interval import interval

#! + + + + + + add item creation as a posible parameter + + + + + 

class Event:

    # Constructors

    def __init__(self,
                 event_name: str,
                 dates_interval: interval,
                 people_keys: list[str], 
                 item_keys: list[str],
                 item_amount: list[int],
                 event_type: str,
                 event_place: str):

        self.event_name = event_name
        self.dates = dates_interval
        self.people_keys = people_keys
        self.item_keys = item_keys
        self.item_amount = item_amount
        self.event_type = event_type
        self.event_place = event_place

    # Parameter validation methods
    '''
    These methods are made for evaluating the if parameters are valid
    
    These could be moved to some other classes 
    '''

    @staticmethod
    def valid_date(day, month, year):
        return False #no implementado

    @staticmethod
    def valid_period(starting_date, ending_date):
        return False #no implementado

    # Parameter General Operations
    '''
    These methods is made for making possible operations between parameters
    '''

    def get_interval(self):
        return self.dates
    
    def get_starting_date(self) -> datetime.datetime:
        return self.dates.start_date
    
    def get_ending_date(self) -> datetime.datetime: 
        return self.dates.end_date
    
    def get_item_keys(self):
        return self.item_keys
    
    def get_item_amount(self):
        return self.item_amount
    
    def get_name(self):
        return self.event_name
    
    # Data format method

    def get_as_dictionary(self):

        output = {
            "NAME": self.event_name,
            "DATE_START": self.get_starting_date().__str__(),
            "DATE_END": self.get_ending_date().__str__(),
            "PEOPLE_KEYS": self.people_keys,
            "ITEM_KEYS": self.item_keys,
            "ITEM_AMOUNT": self.item_amount,
            "EVENT_TYPE": self.event_type,
            "EVENT_PLACE": self.event_place
        }

        return output
    
    @staticmethod
    def dictionary_to_event(event_as_dictionary):
        
        start_date = datetime.datetime.strptime(event_as_dictionary["DATE_START"], '%Y-%m-%d %H:%M:%S')
        end_date = datetime.datetime.strptime(event_as_dictionary["DATE_END"], '%Y-%m-%d %H:%M:%S')
        the_interval = interval(start_date, 
                                end_date)

        output = Event(event_as_dictionary["NAME"],
                       the_interval,
                       event_as_dictionary["PEOPLE_KEYS"],
                       event_as_dictionary["ITEM_KEYS"],
                       event_as_dictionary["ITEM_AMOUNT"],
                       event_as_dictionary["EVENT_TYPE"],
                       event_as_dictionary["EVENT_PLACE"])
        
        return output
    
    @staticmethod
    def get_event_type_list():
        output = [
            "undeterminated",
            "maneuver",
            "reparation",
            "medic operation",
            "minig operation",
            "work meeting",
            "comercial operation",
            "defencive operation"
        ]

        return output

    




        