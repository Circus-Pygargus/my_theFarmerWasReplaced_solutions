from __builtins__ import *

def auto_select_recipe():
    current_hay = num_items(Items.Hay)
    current_wood = num_items(Items.Wood)
    current_carrots = num_items(Items.Carrot)
    current_pumpkins = num_items(Items.Pumpkin)

    if current_hay <= current_wood and current_hay <= current_carrots and current_hay <= current_pumpkins:
        hay_loop()
    elif current_wood <= current_hay and current_wood <= current_carrots and current_wood <= current_pumpkins:
        wood_loop()
    elif current_pumpkins <= current_hay and current_pumpkins <= current_wood and current_pumpkins <= current_carrots:
        pumpkin_loop()
    else:
        carrot_loop()
