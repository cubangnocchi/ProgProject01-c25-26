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
    
    def get_starting_date(self):
        return self.dates.start_date
    
    def get_ending_date(self):
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
            "DATE_START": self.get_starting_date(),
            "DATE_END": self.get_ending_date(),
            "ITEM_KEYS": self.item_keys,
            "ITEM_AMOUNT": self.item_amount
        }

        return output
    
    @staticmethod
    def dictionary_to_event(event_as_dictionary):
        
        Event(event_as_dictionary["NAME"],
              event_as_dictionary["DATE_START"],
              event_as_dictionary["DATE_END"],
              event_as_dictionary["ITEM_KEYS"],
              event_as_dictionary["ITEM_AMOUNT"],)

    # Parameter Construction Methods
    '''
    These methods are made to build parameters
    '''

    # Self Parameters Operations
    '''
    These methods are for operating with self instance parameters
    '''

    # Self Instance Operations
    '''
    These are self instance operations
    '''

    # Instance Operations
    '''
    These methods are for making possible operations between different instances
    '''




        