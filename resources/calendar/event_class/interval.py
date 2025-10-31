import datetime

class interval:
    def __init__(self, the_start_date, the_end_date):
        
        self.start_date = the_start_date
        self.end_date = the_end_date

    def get_dates(self):
        return [self.start_date, self.end_date]
    

    # |||||||||||||||| [ T O O L S ] |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    # - - - - - - - - Non Stacic Methods - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    def is_it_contained(self, inner_interval):
        out_dates = self.get_dates()
        inner_dates = inner_interval.get_dates()

    # - - - - - - - - Static Methods - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @staticmethod
    def is_it_overlaping(interval_one, interval_two):
        #gets dates from intervals
        dates_one = interval_one.get_dates()
        dates_two = interval_two.get_dates()
        
        #if the end of one is before the start of an other, the  intervals are not overlaping
        if(dates_one[1] <= dates_two[0] or dates_two[1] <= dates_one[0]):
            return False
        
        return True
    
    
    def is_it_inside(interval_one, interval_two):
        #gets dates from intervals
        dates_one = interval_one.get_dates()
        dates_two = interval_two.get_dates()


        