clear() # have grass in each field and move drone at bottom left of the farm
while True:
    for i in range(3):
        for j in range(3):
            if can_harvest():
                harvest()
                # I need some hay to be able to plant enough carrots to get next unlock
                if num_items(Items.Hay) > 50:
                    plant(Entities.Bush)
            move(North)
        move(East)
