from __builtins__ import *

def power_loop():
    continue_main_loop = True
    needed_seeds_nb = 3 * get_world_size()**2
    is_first_loop = True
    harvested_times = 0
    max_harvested_times = 2 * get_world_size()**2
    fields_positions = []
    field_petals_nbs = []

    while continue_main_loop:
        if get_pos_x() == 0 and num_items(Items.Sunflower_Seed) <= needed_seeds_nb:
            if needed_seeds_nb > num_items(Items.Carrot):
                carrot_loop()

            trade(Items.Sunflower_Seed, needed_seeds_nb)

        for field_id in range(get_world_size()):
            if is_first_loop:
                fields_positions.insert(field_id, (get_pos_x(), get_pos_y()))

                # harvest remaining entity
                if get_entity_type() != None:
                    while not can_harvest():
                        do_a_flip()
                    harvest()

                if get_pos_x() + 1 == get_world_size() and get_pos_y() + 1 == get_world_size():
                    is_first_loop = False

            handle_ground(Grounds.Soil)
            plant(Entities.Sunflower)
            handle_water()
            field_petals_nbs.insert(field_id, measure())

            if get_pos_x() + 1 == get_world_size() and get_pos_y() + 1 == get_world_size():
                while harvested_times <= max_harvested_times:
                    max_petals_nb = max(field_petals_nbs)
                    field_to_harvest_id = get_list_index(field_petals_nbs, max_petals_nb)
                    field_to_harvest_pos = fields_positions[field_to_harvest_id]
                    go_to_field(field_to_harvest_pos[0], field_to_harvest_pos[1])

                    while not can_harvest():
                        do_a_flip()
                    harvest()
                    harvested_times += 1

                    field_petals_nbs.remove(max_petals_nb)

                    plant(Entities.Sunflower)

                    handle_water()
                    field_petals_nbs.insert(field_to_harvest_id, measure())

            move(North)

        move(East)

        if harvested_times > max_harvested_times:
            go_to_field(0, 0)
            continue_main_loop = False
