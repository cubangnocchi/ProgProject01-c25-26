

class Human:
    def __init__(self, name, type, day_born):
        self.name = name
        self.type = type #engineer, captain, kid, doctor, political comisair, 
        self.day_born = day_born

    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type

    def get_age(self, actualdate):
        return self.day_born - actualdate