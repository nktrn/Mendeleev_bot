import re


def check_en(text):
    return True if re.fullmatch('[a-zA-Z]+', text) else False
