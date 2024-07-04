from __builtins__ import *

# Returns first index with given value, or None if value wasn't found in given list
def get_list_index(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i

    return None
