from __builtins__ import *

def pumpkin_loop():
    needed_seeds_nb = get_world_size()**2
    is_first_loop = True
    harvested_times = 0
    harvest_wanted_nb = get_world_size()**2

    while harvested_times <= harvest_wanted_nb:
        if get_pos_x() == 0:
            handle_tank_nb()
            has_empty_field = False

            if num_items(Items.Pumpkin_Seed) < needed_seeds_nb:
                if num_items(Items.Carrot) < needed_seeds_nb:
                    carrot_loop()
                trade(Items.Pumpkin_Seed, needed_seeds_nb)

        for i in range(get_world_size()):
            if can_harvest() and get_entity_type() != Entities.Pumpkin:
                harvest()

            if is_first_loop:
                handle_ground(Grounds.Soil)

            if not can_harvest() or get_entity_type() != Entities.Pumpkin:
                has_empty_field = True

            plant(Entities.Pumpkin)
            handle_water()

            move(North)

        move(East)

        if get_pos_x() == 0:
            is_first_loop = False

        if get_pos_x() == 0 and get_pos_y() == 0 and not has_empty_field:
            harvest()
            harvested_times += 1
