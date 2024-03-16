
import re

def parse_link(string):
    if (match := re.fullmatch(r'<a href="(.+?)">(.*?)(?:<\/a>)', string)):
        return match.groups()[::-1]
