import datetime
from src.calendar.event_class.interval import interval

class Event:

    # Constructors

    def __init__(self, event_name, starting_date, ending_date, objects_keys):
        self.event_name = event_name
        self.dates = interval(starting_date, ending_date)
        self.objects_keys = objects_keys

    # Parameter validation methods
    '''
    These methods are made for evaluating the if parameters are valid
    
    These could be moved to some other classes 
    '''

    @staticmethod
    def valid_date(day, month, year):
        return False

    @staticmethod
    def valid_period(starting_date, ending_date):
        return False

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




        