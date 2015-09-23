import re


def binary(s):
    return re.match(r'[01]', s)


def binary_even(s):
    return re.match(r'[0-1]+0$', s)



def hex(s):
    return re.match(r'[^G-Z][\dA-F]+', s)


def word(s):
    return re.match(r'^[0-9a-zA-Z-]*[a-zA-Z]$', s)


def words(s, count= None):
     list_words = re.split('\s',s)
     if count:
        if count != len(list_words):
            return None
        else:
            pass
        if None in [re.match(r'[\w/-]*[a-z]+$', w) for s in list_words]:
            return None
        else:
            return list_words
