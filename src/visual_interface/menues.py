def main_menue():

    options = ["1"] #add option keys here

    while True:
       print("---[Main Menue]---")
       print("------------------")
       print("press a [key] + [Enter↲] to select one of the following options:")
       print("[1] - ")
       #.............
       option_selected = input()
       if not (option_selected in options):
           print("wrong imput, try again")
           print(" ")
       else:
           print("option selected")
           break

    