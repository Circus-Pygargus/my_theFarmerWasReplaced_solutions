from __builtins__ import *

def wood_loop():
    current_loop = 0
    wanted_loops = get_world_size()**2

    while current_loop <= wanted_loops:
        for i in range(get_world_size()):
            if can_harvest():
                harvest()

            plant(Entities.Bush)

            move(North)

        move(East)

        if get_pos_x() == 0:
            current_loop +=1
