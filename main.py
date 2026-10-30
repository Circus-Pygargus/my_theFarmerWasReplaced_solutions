clear() # have grass in each field and move drone at bottom left of the farm
while True:
    for i in range(3):
        for j in range(3):
            if can_harvest():
                harvest()
                if num_items(Items.Hay) > 50:
                    if num_items(Items.Wood) < 50:
                        plant(Entities.Bush)
                    else:
                        if get_ground_type() != Grounds.Soil:
                            till()
                        plant(Entities.Carrot)     
                move(North)
        move(East)
