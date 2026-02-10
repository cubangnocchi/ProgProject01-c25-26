from src.calendar.event_class.interval import interval
from src.calendar.event_class.event import Event
from src.inventory.human import Human
from src.inventory.inventory import Inventory
from src.inventory.item import Item

from src.visual_interface import menues
import datetime

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
           