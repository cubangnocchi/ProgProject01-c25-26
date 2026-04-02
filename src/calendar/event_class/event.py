import datetime
from src.calendar.event_class.interval import interval

#! + + + + + + add item creation as a posible parameter + + + + + 

class Event:

    # Constructors

    def __init__(self,
                 event_name: str,
                 dates_interval: interval, 
                 item_keys,
                 item_amount):

        self.event_name = event_name
        self.dates = dates_interval
        self.item_keys = item_keys
        self.item_amount = item_amount

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
            "ITEM_KEYS": self.item_keys,
            "ITEM_AMOUNT": self.item_amount
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
                       event_as_dictionary["ITEM_KEYS"],
                       event_as_dictionary["ITEM_AMOUNT"],)
        
        return output
    
    @staticmethod
    def event_type_list():
        output = [
            "undeterminated"
            "maneuver",
            "reparation",
            "medic operation",
            "minig operation",
            "work meeting",
            "comercial operation",
            "defencive operation"
        ]

    




        