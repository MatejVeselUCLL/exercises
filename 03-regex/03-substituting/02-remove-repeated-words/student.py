import re
def remove_repeated_words(string):
    return re.sub(r'(\b\w+\b)(?: \1)+', r'\1', string)