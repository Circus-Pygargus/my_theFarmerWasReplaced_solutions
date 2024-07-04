from __builtins__ import *

def wood_loop():
    current_loop = 0
    wanted_loops = get_world_size()**2
    needed_fertilizer = get_world_size()**2

    while current_loop <= wanted_loops:
        if num_items(Items.Fertilizer) < needed_fertilizer:
            if 10 * num_items(Items.Pumpkin) < needed_fertilizer:
                pumpkin_loop()
            trade(Items.Fertilizer, needed_fertilizer)

        if get_pos_x() == 0:
            handle_tank_nb()

        for i in range(get_world_size()):
            if can_harvest():
                harvest()
                handle_water()

            # Alternate tree and bush in grid
            handle_ground(Grounds.Soil)
            if get_pos_x() % 2 == get_pos_y() % 2:
                plant(Entities.Tree)
                use_item(Items.Fertilizer)
            else:
                plant(Entities.Bush)
            handle_water()

            move(North)

        move(East)

        if get_pos_x() == 0:
            current_loop +=1
            handle_tank_nb()
