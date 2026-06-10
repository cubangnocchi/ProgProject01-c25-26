from datetime import datetime

class Human:
    def __init__(self,
                 name: str, 
                 speciality: str,
                 status: str, 
                 day_born: datetime):
        
        self.name = name
        self.speciality = speciality #engineer, captain, kid, doctor, political comisair, 
        self.status = status
        self.day_born = day_born

    def get_name(self):
        return self.name
    
    def get_speciality(self):
        return self.speciality
    
    def get_status(self):
        return self.status

    def get_age(self, actualdate: datetime):
        age = actualdate.year - self.day_born.year

        #just in case this year your birthday hasn't ocurred yet
        if((actualdate.month, actualdate.day)<(self.day_born.month, self.day_born.day)):
            age -= 1

        return age
    def convert_to_dictionary(self):
        
        output = {
            "NAME": self.name,
            "SPECIALITY": self.speciality,
            "STATUS": self.status,
            "BORN_DATE": (self.day_born.__str__())
        }

        return output
    
    @staticmethod
    def convert_from_dictionary_to_human(data: dict):
        name = data["NAME"]
        speciality = data["SPECIALITY"]
        status = data["STATUS"]
        day_born = datetime.strptime(data["BORN_DATE"], '%Y-%m-%d %H:%M:%S')

        output = Human(name, speciality, status, day_born)

        return output
    
    @staticmethod
    def get_status_list():
        status = [
            "passenger",
            "crew member",
            "captain",
            "first oficial",
            "second oficial",
            "mining oficial",
            "defence oficial",
            "soldier",
            "corporation representative"
        ]

        return status

    @staticmethod
    def get_specialization_list():
        specialization =[
            "unspecialized",
            "nuclear engineer",
            "software engineer",
            "weapons engineer",
            "electric engineer",
            "communications specialist",
            "mining specialist",
            "weapons specialist",
            "reparation specialist",
            "mechanic",
            "first aid",
            "medic",
            "pilot",
            "bureaucrat"
        ]

        return specialization