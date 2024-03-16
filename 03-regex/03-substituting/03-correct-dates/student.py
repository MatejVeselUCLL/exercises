import re
def correct_dates(string):
    return re.sub(r'(\d+)/(\d+)/', r'\2/\1/', string) # Documentation: "Changed in version 3.7: Only characters that can have special meaning in a regular expression are escaped. As a result, '!', '"', '%', "'", ',', '/', ':', ';', '<', '=', '>', '@', and "`" are no longer escaped."