from src.calendar.event_class.interval import interval
from src.calendar.event_class.event import Event
from src.inventory.human import Human
from src.inventory.inventory import Inventory
from src.inventory.item import Item
from src.calendar.calendar import Calendar
from src.visual_interface import menues
from datetime import datetime
from src.data_base import data_management
from src.visual_interface.menue import Menue

def menue_class_test():
    options = {
        "1": "patata",
        "2": "lololo",
        "x": "lululu"
    }
    mmmmm = Menue(
        "el menú",
        options,
        "escribe y da enter ahí"
    )

    a = mmmmm.print()
    print(a)


def calendario_test():
    FILEPATH = 'src/data_base/test.json'
    inter10 = interval(datetime(2010, 10, 10), datetime(2010, 11, 11))
    inter11 = interval(datetime(2011, 10, 10), datetime(2011, 11, 11))
    inter12 = interval(datetime(2012, 10, 10), datetime(2012, 11, 11))
    inter13 = interval(datetime(2013, 10, 10), datetime(2013, 11, 11))
    inter14 = interval(datetime(2014, 10, 10), datetime(2014, 11, 11))
    inter15 = interval(datetime(2015, 10, 10), datetime(2015, 11, 11))
    inter16 = interval(datetime(2016, 10, 10), datetime(2016, 11, 11))
    inter17 = interval(datetime(2017, 10, 10), datetime(2017, 11, 11))
    
    e01 = Event("10", inter10, [], [])
    e02 = Event("11", inter11, [], [])
    e03 = Event("12", inter12, [], [])
    e04 = Event("13", inter13, [], [])
    e05 = Event("14", inter14, [], [])
    e06 = Event("15", inter15, [], [])
    e07 = Event("16", inter16, [], [])
    e08 = Event("17", inter17, [], [])
    
    places = {
        "sala01": [e01, e02, e03, e07],
        "sala02": [e04, e05, e06, e08]
    }

    papa = Calendar(places, datetime(2020, 10, 10))
   

    lolo = Inventory([],[])
    data = data_management.convert_objects_to_json(papa, lolo)

    data_management.save_data(FILEPATH, data)

    data = data_management.load_data(FILEPATH)

    data = data_management.convert_json_to_objects(data)
    
    
    papa = data[0]
    
    papa.insert_event_in_place(e01, "sala02")

    
    data = data_management.convert_objects_to_json(papa, lolo)

    data_management.save_data(FILEPATH, data)

'''
def test_intervals():

    f1 = datetime.datetime(2200, 10, 10)
    f2 = datetime.datetime(2250, 10, 10)
    f3 = datetime.datetime(2240, 10, 10)
    f4 = datetime.datetime(2270, 10, 10)

    a = interval(f1,f2)
    
    b = interval(f3,f4)
    
    print("patata")
    
    print(interval.is_it_overlaping(a, b))
    print(interval.is_it_overlaping(b, a))

def test_event():
    print("testing events")

    
    f1 = datetime.datetime(2200, 10, 10)
    f2 = datetime.datetime(2250, 10, 10)

    evento01 = Event("patata", f1, f2, "01")

    print(evento01.get_ending_date())

def date_creation_test():
    
    actual_date = datetime.datetime(2026,2,3,14,46)
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    elevento = menues.event_creation_menue(actual_date)
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(elevento.get_starting_date())
    
    print(elevento.get_ending_date())

    
    print(elevento.get_name())
    
def presetInventoryCreator():
    print("preset inventory created")

    cosa01 = (Item("comida", True)).set_amount(10)
    cosa02 = Item("cosaESpecialESpacial", False)

    listadeitems = [cosa01,cosa02]

    fechadenacimiento = datetime.datetime(2000,5,5)
    persona01 = Human("Pepito","Ingeniero", fechadenacimiento)
    persona02 = Human("Juanita", "Astrofísica", fechadenacimiento)

    listadegente = [persona01,persona02]

    elinventario = Inventory(listadeitems, listadegente)

    return elinventario
           '''