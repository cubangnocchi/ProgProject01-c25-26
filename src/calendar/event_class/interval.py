import datetime

class interval:
    def __init__(self, the_start_date, the_end_date):
        
        self.start_date = the_start_date
        self.end_date = the_end_date

    def get_dates(self):
        return [self.start_date, self.end_date]
    

    # |||||||||||||||| [ T O O L S ] |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    # - - - - - - - - Non Stacic Methods - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    # not done
    def is_it_contained(self, inner_interval):
        out_dates = self.get_dates()
        inner_dates = inner_interval.get_dates()

    # - - - - - - - - Static Methods - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @staticmethod
    def is_it_overlaping(interval_one, interval_two):
        #gets dates from intervals
        dates_one = interval_one.get_dates()
        dates_two = interval_two.get_dates()
        
        #if the begining of a period is inside the other period, then it's overlaping
        if(dates_one[0] >= dates_two[0] and dates_one[0] <= dates_two[1]):
            return True
        if(dates_two[0] >= dates_one[0] and dates_two[0] <= dates_one[1]):
            return True
        
        return False
    
    @staticmethod
    def is_it_inside(interval_one, interval_two):
        #gets dates from intervals
        dates_one = interval_one.get_dates()
        dates_two = interval_two.get_dates()

        #........ 
    
    @staticmethod
    def distance(interval_first, interval_second):

        first_end_date = interval_first.get_dates[1]
        second_start_date = interval_first.get_dates[0]

        return second_start_date - first_end_date 

    @staticmethod
    def available_period(interval_first, interval_second):
        
        return interval_first.get_dates[1], interval_second.get_dates
        


        