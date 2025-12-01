

class Item:

    def __init__(self, type):
        self.type = type
        self.inUse = False

    def is_it_in_use (self):
        return self.inUse
    
    def set_in_use(self, value):
        self.inUse = value

    



    