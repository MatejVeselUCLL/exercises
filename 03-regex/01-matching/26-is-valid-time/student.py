import re
def is_valid_time(string):
    hours = r'(([01][0-9])|([2][0-4]))'
    minutes = r'[0-5][0-9]'
    seconds = minutes
    miliseconds = r'[0-9]{3}'

    return re.fullmatch(f'{hours}:{minutes}:{seconds}(.{miliseconds})?', string)
