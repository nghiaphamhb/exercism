"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    if len(list_one) == 0 and len(list_two) != 0:
        return SUBLIST
    if len(list_two) == 0 and len(list_one) != 0:
        return SUPERLIST   
    
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two) and len(list_one) <= len(list_two):
        return SUBLIST
    elif is_superlist(list_one, list_two) and len(list_one) >= len(list_two):
        return SUPERLIST
    else:
        return UNEQUAL


def is_sublist(list_one, list_two):
    for i in range(len(list_two) - len(list_one) + 1):
        if list_two[i:i + len(list_one)] == list_one:
            return True
    return False

def is_superlist(list_one, list_two):
    for i in range(len(list_one) - len(list_two) + 1):
        if list_one[i:i + len(list_two)] == list_two:
            return True
    return False
