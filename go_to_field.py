from __builtins__ import *

def go_to_field(wanted_pos_x, wanted_pos_y):
    is_at_pos_x = False
    is_at_pos_y = False

    while not is_at_pos_x or not is_at_pos_y:
        if get_pos_x() < wanted_pos_x:
            move(East)
        elif get_pos_x() > wanted_pos_x:
            move(West)
        else:
            is_at_pos_x = True

        if get_pos_y() < wanted_pos_y:
            move(North)
        elif get_pos_y() > wanted_pos_y:
            move(South)
        else:
            is_at_pos_y = True
