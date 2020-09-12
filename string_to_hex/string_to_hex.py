#
# convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"
# Create a Function that takes a strings characters as ASCII and returns each characters hexadecimal value as a string.


def convert_to_hex(txt):
    return ' '.join(hex(ord(i))[2:] for i in txt)


def convert_to_hex_alt(txt):
    return ' '.join(hex(ord(i))[2:] for i in txt)

