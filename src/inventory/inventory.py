from src.inventory.human import Human
from src.inventory.item import Item

class Inventory:
    def __init__(self, items: dict[str, Item], people: dict[str, Human], next_key: int):
        self.items = items
        self.people = people
        self.next_key = next_key #!each time an item or something is added, this goes ++ 
    
    def get_items(self):
        return self.items
    
    def get_people(self):
        return self.people
    
    def get_item(self, key: str):
        return self.items[key]
    
    def get_person(self, key: str):
        return self.people[key]
    
    def get_items_keys(self):
        return list(self.items.keys())
    
    def get_people_keys(self):
        return list(self.people.keys())
    
    def convert_to_dict(self):
        item_keys = self.get_items_keys()
        people_keys = self.get_people_keys()
        converted_items = {}
        converted_humans = {}

        for key in item_keys:
            converted_items[key] = self.items[key].convert_to_dictionary()

        for key in people_keys:
            converted_humans[key] = self.people[key].convert_to_dictionary()

        output = {
            "ITEMS": converted_items,
            "PEOPLE": converted_humans 
        }

        return output
    
    @staticmethod
    def convert_dict_to_inventory(inventory_dict: dict[str, dict]):
        
        items_as_dict = inventory_dict["ITEMS"]
        humans_as_dict = inventory_dict["PEOPLE"]

        item_keys = list(items_as_dict.keys())
        people_keys = list(humans_as_dict.keys())

        

        for key in item_keys:

        


    
    #! hay que ver cómo poder hacer referencia a los items por un index mmmmmmmmmmmmmmmmmmmmmmm
    #! convierte todo a diccionario -_-
    
    
        


'''
++++++++++++++++++++++++++++++++++++++++++++

//overengeenering and overcomplicated and overengineered
//aaaaaaaaaaa
//

make a "calendar" with how much available items we have in each period

in it I need to have defined periods from one relevant date to an other...
like:

today - next event start, an other level start, the end of the first one, the end of the seecond one, an other...... the end of the last one, the end

- first, organice all events (no mater its place)
- a method that takes a date and search for the next relevant date, each time an event is checked from start to end it jumps into the next one
- end up with a list of concatenated intervales with how much items are available in each period
- for creating an event its period must be compared to the group of intervals it overlap...
  - run though the inventary periods, 
  - once it gets into an interval, save them till the next dont overlap
  - brake
  - take the minimun available value of each item
  - 

'''