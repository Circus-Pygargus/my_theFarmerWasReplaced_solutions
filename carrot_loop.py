from __builtins__ import *

def carrot_loop():
    current_loop = 0
    wanted_loops = get_world_size()**2
    needed_seeds_nb = get_world_size()**2
    needed_fertilizer = get_world_size()**2

    while current_loop <= wanted_loops:
        if get_pos_x() == 0:
            if num_items(Items.Carrot_Seed) < needed_seeds_nb:
                if num_items(Items.Hay) < needed_seeds_nb:
                    hay_loop()
                elif num_items(Items.Wood) < needed_seeds_nb:
                    wood_loop()
                else:
                    trade(Items.Carrot_Seed, needed_seeds_nb)

            if num_items(Items.Fertilizer) < needed_fertilizer:
                if 10 * num_items(Items.Pumpkin) < needed_fertilizer:
                    pumpkin_loop()
                trade(Items.Fertilizer, needed_fertilizer)

        for i in range(get_world_size()):
            if can_harvest():
                harvest()
                handle_water()

            if current_loop == 0:
                handle_ground(Grounds.Soil)

            plant(Entities.Carrots)
            use_item(Items.Fertilizer)
            handle_water()

            move(North)

        move(East)

        if get_pos_x() == 0:
            current_loop += 1
            handle_tank_nb()
