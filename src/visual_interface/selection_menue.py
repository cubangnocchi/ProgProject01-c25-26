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

            if(selected_option not in option_keys_list):
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

            if(selected_option not in option_keys_list):
                print("ERROR: option not available, try again:")
                print()
            else:
                return self.options[selected_option]
    
    @staticmethod
    def create_numerable_dict_from_list(the_list: list[str]):
        output_dictionary = {}
        i = 0
        for element in the_list:
            output_dictionary[i] = element
            i += 1

        return output_dictionary

            

            
        
        
        