from __builtins__ import *

clear()

while True:
    for i in range(get_world_size()):
        if can_harvest():
            harvest()
            if get_ground_type() != Grounds.Soil:
                till()
            # carrot seed costs 1 hay + 1 wood
            # At this point, I was sure to have enough hay (more than 1k) but sure I would not have enough wood (less than 100)
            # this code is used to unlock variables and functions (need 150 carrots)
            # edit : I did'nt know each harvest gives 3 carrots ...
            if num_items(Items.Hay) >= 1 and num_items(Items.Wood) >= 1:
                trade(Items.Carrot_Seed)
                plant(Entities.Carrots)
            else:
                plant(Entities.Wood)

        move(North)

    move(East)
