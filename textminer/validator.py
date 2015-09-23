import re


def binary(s):
    return re.match(r'[0-9A-F]+$', s')


def binary_even(s):
    return re.match(r'[0-1]+0$', s)



def hex(s):
    return re.match(r'[0-9A-F]+$', s')


def word(s):
    return re.match(r'^[\w-]*[^\d\W!*]+$', s)


def words(s, = None):
     list_words = re.split(r'\s', s)
     if count:
        if count != len(list_words):
            return None

        if None in [word(x) for x in list_words]:
            return None
        else:
            return list_words
