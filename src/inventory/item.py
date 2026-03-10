

class Item:
    

    def __init__(self, item_type, is_expendable):
        self.item_type = item_type
        self.is_expendable = is_expendable
        self.amount = -1

    def get_type(self):
        return self.item_type

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

    def convert_to_dictionary(self):
        output = {

        }


    



    