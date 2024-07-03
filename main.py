from __builtins__ import *

while True:
    if can_harvest():
        harvest()
        plant(Entities.Bush)

    move(North)
