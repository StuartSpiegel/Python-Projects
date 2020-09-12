from bisect import bisect_left
from itertools import combinations
from time import time
from legacy import xrange
import trie
# This code creates a dictionary file (list of anagrams)


def spawn_Dictionary():
    f = open('anadict.txt', 'r')
    anadict = f.read().split('\n')
    f.close()
    return anadict


scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}


def score_word(word):
    return sum([scores[k] for k in word])


def findwords(rack, anadict):
    rack = ''.join(sorted(rack))
    foundwords = []
    for i in xrange(2, len(rack) + 1):
        for comb in combinations(rack, i):
            ana = ''.join(comb)
            j = bisect_left(anadict, ana)
            if j == len(anadict):
                continue
            words = anadict[j].split()
            if words[0] == ana:
                foundwords.extend(words[1:])
    return foundwords


def walk_trie(trie_node, rack, path=""):
    if trie_node.value is None:
        yield path
    for i in xrange(len(rack)):
        sub_rack = rack[:i] + rack[i+1:]
        if trie_node.nodes.has_key(rack[i]):
            for word in walk_trie(trie_node.nodes[rack[i]], sub_rack, path+rack[i]):
                yield word


if __name__ == "__main__":

    import sys

    if len(sys.argv) == 2:
        rack = sys.argv[1].strip()
    else:
        print("""Usage: python Scrabble_Find_Words.py < yourrack >""")
        exit()
    t = time()
    anadict = spawn_Dictionary()
    print("Dictionary loading time:", (time() - t))
    t = time()
    foundwords = set(findwords(rack, anadict))
    scored = [(score_word(word), word) for word in foundwords]
    scored.sort()
    for score, word in scored:
        print("%d\t%s" % (score, word))
    print("Time elapsed:", (time() - t))

    #   if __name__ == "__main__":
    #     print "Generating trie... "
    #
    # # I've skipped words shorter than 3 characters.
    #     all_words = ((line.strip().lower(), None) for line in open("/usr/share/dict/words") if len(line.strip()) >= 3)
    #     word_trie = trie.Trie(mapping=all_words)
    #     print "Walking Trie... "
    #     print list(walk_trie(word_trie.root, "abcdefg"))
    #
#########################################################################################################
# #scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#          "x": 8, "z": 10}
#
# def calc_score(word):
#     """Calculate the score of a given word."""
#     word_score = 0
#     for x in word:
#         word_score += scores[x]
#     return word_score
#
# def look_up():
#     """Create the variable containing the master list of words."""
#     read_dict = open("sowpods.txt", "r")
#     master = read_dict.read()
#     read_dict.close()
#     master = master.split("\n")
#     return master
#
# word_master = look_up()
#
# def rack_check(f_rack):
#     """Check the letters in the rack against the SOWPOD dictionary and
#     append valid words to a list."""
#     valid_list = []
#     for item in word_master:
#         letter_bank = list(f_rack)
#         for letter in item:
#             if letter in letter_bank:
#                 valid = True
#                 letter_bank.remove(letter)
#             else:
#                 valid = False
#                 break
#         if valid == True:
#             valid_list.append(item)
#     return valid_list
#
# def dict_maker():
#     """Create a dictionary of the words with their scores."""
#     valid_dict = {}
#     f_list = rack_check(list((raw_input("Letters: ")).lower()))
#     for i in f_list:
#         valid_dict[i] = calc_score(i)
#     return valid_dict
#
# def list_print():
#     """Print a list of the words in descending order of value."""
#     dict = dict_maker()
#     sort_dict = sorted(dict.items(), key=lambda k: k[1], reverse=True)
#     for x in sort_dict:
#         print x[0], "-", x[1]
#
# list_print()
