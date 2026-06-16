from src.calendar.event_class.interval import interval
from src.calendar.event_class.event import Event
from src.inventory.human import Human
from src.inventory.inventory import Inventory
from src.inventory.item import Item
from src.calendar.calendar import Calendar
from datetime import datetime
from src.data_base import data_management
from src.visual_interface import menues
from src.manager import restrictions_data
from src.manager import data_search
from src.manager import manager
from src.manager import restrictions

#global variables
FILEPATH = 'src/data_base/save01.json'
    
raw_data = data_management.load_data(FILEPATH)
data = data_management.convert_json_to_objects(raw_data)
main_calendar = data[0]
main_inventory = data[1]

elevento = main_calendar.get_event_list()[0]

lista_de_errores = restrictions.check_event(elevento, main_calendar, main_inventory)

for blabla in lista_de_errores:
    print(blabla)

