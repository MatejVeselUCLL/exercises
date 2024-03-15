import re
def only_digits(string):
    # return re.fullmatch("(0|1|2|3|4|5|6|7|8|9)*", string)
    return re.fullmatch("[0123456789]*", string)