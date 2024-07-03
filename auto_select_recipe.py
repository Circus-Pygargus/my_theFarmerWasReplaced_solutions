from __builtins__ import *

def auto_select_recipe():
    current_hay = num_items(Items.Hay)
    current_wood = num_items(Items.Wood)
    current_carrots = num_items(Items.Carrot)

    if current_hay <= current_wood and current_hay <= current_carrots:
        hay_loop()
    elif current_wood <= current_hay and current_wood <= current_carrots:
        wood_loop()
    else:
        carrot_loop()
