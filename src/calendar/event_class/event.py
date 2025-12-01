import datetime

class Event:

    # Constructors

    def __init__(self, event_name, starting_date, ending_date, objects):
        self.event_name = event_name
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.objects = objects

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




        