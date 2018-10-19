from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]

def get_current_room():
	return current_room
def set_current_room(new_room):
	current_room = new_room
