import re
def is_number(string):
    return re.fullmatch('[0-9]+(\\.[0-9]+)?', string)
    # Q& Why does this match an empty string?


