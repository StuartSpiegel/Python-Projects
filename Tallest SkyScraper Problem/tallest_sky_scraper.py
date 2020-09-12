#
# A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of
# the tallest building is 4 (second-most right column).
# tallest_skyscraper([
#  [0, 0, 0, 0],
#  [0, 1, 0, 0],
#  [0, 1, 1, 0],
#  [1, 1, 1, 1]
# ]) ➞ 3
#
# tallest_skyscraper([
#  [0, 1, 0, 0],
#  [0, 1, 0, 0],
#  [0, 1, 1, 0],
#  [1, 1, 1, 1]
# ]) ➞ 4
#
# tallest_skyscraper([
#  [0, 0, 0, 0],
#  [0, 0, 0, 0],
#  [1, 1, 1, 0],
#  [1, 1, 1, 1]
# ]) ➞ 2


def tallest_skyscraper(lst):
    return sum(1 for i in lst if sum(i) > 0)


def tallest_skyscraper_alt(lst):
    return max(sum(i) for i in zip(*lst))
