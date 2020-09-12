# Create a function that takes a variable number of groups of items, and returns the number of ways the items can be
# arranged, with one item from each group. Order does not matter.
#
# combinations(2, 3) ➞ 6
#
# combinations(3, 7, 4) ➞ 84
#
# combinations(2, 3, 4, 5) ➞ 120
#
from numpy import prod


def combinations(*items):
    prod = 1
    for i in items:
        if i > 0:
            prod *= i
    return prod


def combinations_alt(*a):
    return prod([x for x in a if x > 0])

