from __builtins__ import *

clear()

while True:
    if can_harvest():
        harvest()
        plant(Entities.Bush)

    move(North)
