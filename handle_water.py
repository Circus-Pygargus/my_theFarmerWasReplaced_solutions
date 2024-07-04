from __builtins__ import *

def handle_water():
    wanted_water = 0.9

    if num_items(Items.Water_Tank) == 0:
        return

    if get_water() < wanted_water:
        use_item(Items.Water_Tank)
