from datetime import datetime

class Human:
    def __init__(self, name: str, speciality: str, day_born: datetime):
        self.name = name
        self.speciality = speciality #engineer, captain, kid, doctor, political comisair, 
        self.day_born = day_born

    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type

    def get_age(self, actualdate):
        return self.day_born - actualdate #!revisaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaar
    
    def convert_to_dictionary(self):
        
        output = {
            "NAME": self.name,
            "SPECIALITY": self.type,
            "BORN_DATE": (self.day_born.__str__())
        }

        return output
    
    @staticmethod
    def convert_from_dictionary_to_human(data: dict):
        name = data["NAME"]
        speciality = data["SPECIALITY"]
        day_born = datetime.strptime(data["BORN_DATE"], '%Y-%m-%d %H:%M:%S')

        output = Human(name, speciality, day_born)

        return output
    
    @staticmethod
    def human_type_dict():

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

        specialization =[
            "unspecialized",
            "nuclear engineer",
            "software engineer",
            "weapons engineer",
            "electric engineer",
            "communications specialist",
            "mining specialist",
            "weapons specialist",
            "reparation specialist"
            "mechanic"
            "first aid"
            "medic"
            "bureaucrat"
        ]

        output = {
            "STATUS": status,
            "SPECIALIZATION": specialization
        }