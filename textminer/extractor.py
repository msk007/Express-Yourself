import re
import pytest
import textminer


def phone_numbers():
    return re.findall(r'\(?\d{3}\W*\d{3}\-?\d{4}')
