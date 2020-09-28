import re


def check_en(text):
    if re.fullmatch('[a-zA-Z]+', text):
        return True
    else:
        return False
