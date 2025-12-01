

class Item:
    

    def __init__(self, type, is_expendable):
        self.type = type
        self.is_expendable = is_expendable
        self.amount = -1

    def get_type(self):
        return self.type

    def is_it_expendable(self):
        return self.is_expendable

    def have_amount(self):
        if(self.amount == -1):
            return False
        return True
    def get_amount(self):
        return self.amount

    def set_amount(self, new_amount):
        self.amount = new_amount


    



    