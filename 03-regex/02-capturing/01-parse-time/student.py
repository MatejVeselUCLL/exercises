import re

def parse_time(string):
    h = r'[01][0-9]|2[0-4]'
    m = r'[0-5][0-9]'
    s = m
    ms = r'[.:][0-9]{3}'

    if (match := re.fullmatch(f'({h}):({m}):({s})({ms})?', string)):
        h, m, s, ms = match.groups('.000')
        ms = ms[1:]
        return (int(h), int(m), int(s), int(ms))
    
# Tests
# print(parse_time("00:00:00:001"))
# print(parse_time("11:12:13"))
# print(parse_time("37:42:09.642"))
    