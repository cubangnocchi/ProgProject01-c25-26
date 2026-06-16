
class Item:

    def __init__(self, item_name: str, item_type: str, is_expendable: bool):
        self.name = item_name
        self.item_type = item_type
        self.is_expendable = is_expendable
        self.amount = -1
    
    def get_name(self):
        return self.name
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

        is_expendable_as_int = 0
        if self.is_expendable:
            is_expendable_as_int = 1
        
        output = {
            "ITEM_NAME": self.name,
            "ITEM_TYPE": self.item_type,
            "IS_EXPENDABLE": is_expendable_as_int,
            "AMOUNT": self.amount
        }
        
        return output
    
    @staticmethod
    def convert_dictionary_to_item(dictionary: dict):

        item_type = dictionary["ITEM_TYPE"]
        item_name = dictionary["ITEM_NAME"]

        is_expendable = False
        if(dictionary["IS_EXPENDABLE"] == "1"):
            is_expendable = True

        amount = int(dictionary["AMOUNT"])

        output = Item(item_name, item_type, is_expendable)
        output.set_amount(amount)

        return output
    
    @staticmethod
    def item_type_list():
        output = [
           #"",
            "life suport",
            "medic",
            "tool",
            "bio-hazard",
            "radio-hazard",
            "chemical hazard",
            "bio-hazard protection",
            "radio-hazard protection",
            "chemical hazard protection",
            "vacuum protection",
            "weapon",
            "cargo",
            "none"
        ]

        return output
    