from __builtins__ import *

def handle_tank_nb():
    needed_wood = 5

    if num_items(Items.Wood) < needed_wood:
        wood_loop()

    if num_items(Items.Water_Tank) == 0 or num_items(Items.Water_Tank) < num_items(Items.Empty_Tank):
        trade(Items.Empty_Tank)
