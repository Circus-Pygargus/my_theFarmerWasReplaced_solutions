clear() # have grass in each field and move drone at bottom left of the farm
while True:
    for i in range(3):
        for j in range(3):
            if can_harvest():
                harvest()
                plant(Entities.Bush)
            move(North)
        move(East)
