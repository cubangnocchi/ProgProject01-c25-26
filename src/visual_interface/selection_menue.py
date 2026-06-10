from src.inventory.item import Item
from src.inventory.human import Human

class SelectionMenue:
    def __init__(self, header: str, options: dict[str, str], instruction: str):
        self.header = header
        self.options = options #(asigned input key, the option)
        self.instruction = instruction
    
    def print_get_key(self):
        
        option_keys_list = list(self.options.keys())

        while True:
            print(f"---[{self.header}]---")

            for key in option_keys_list:
                print(f"[{key}] - {self.options[key]}")
            
            print(self.instruction)

            selected_option = input()

            if(not (selected_option in option_keys_list)):
                print("ERROR: option not available, try again:")
                print()
            else:
                return selected_option
            
    def print_get_option(self):
        
        option_keys_list = list(self.options.keys())

        while True:
            print(f"---[{self.header}]---")

            for key in option_keys_list:
                print(f"[{key}] - {self.options[key]}")
            
            print(self.instruction)

            selected_option = input()

            if(not (selected_option in option_keys_list)):
                print("ERROR: option not available, try again:")
                print()
            else:
                return self.options[selected_option]
    
    def get_key(self):

        option_keys_list = list(self.options.keys())
        selected_option = input()

        if(not (selected_option in option_keys_list)):
            print("ERROR: option not available, try again:")
            print()
        else:
            return selected_option
        
    def get_option(self):
        option_keys_list = list(self.options.keys())
        selected_option = input()

        if(not (selected_option in option_keys_list)):
            print("ERROR: option not available, try again:")
            print()
        else:
            return self.options[selected_option]

    @staticmethod
    def create_numerable_dict_from_list(the_list: list[str]):
        output_dictionary = {}
        i = 0
        for element in the_list:
            output_dictionary[str(i)] = element
            i += 1

        return output_dictionary

    @staticmethod
    def item_dict_to_menueable_dict(items: dict[str, Item]):
        key_list = list(items.keys())
        output = {}
        for key in key_list:
            output[key] = items[key].get_name()

        return output 
        
    @staticmethod
    def human_dict_to_menueable_dict(people: dict[str, Human]):
        key_list = list(people.keys())
        output = {}
        for key in key_list:
            output[key] = people[key].get_name()

        return output 
        