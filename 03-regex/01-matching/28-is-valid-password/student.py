import re
# First try.
# def is_valid_password(string):
#     return re.fullmatch(r'[0-9a-zA-Z+\-*.@]{12,}', string) and not re.fullmatch(r'(.)\1\1', string) and not re.fullmatch(r'.*(.).*\1.*\1.*\1.*', string)

# Second try.
# def is_valid_password(string):
#     must_have_chars = re.fullmatch(r'[0-9]+[a-z]+[A-Z]+[+\-*/.@]+' ,string)
#     print(must_have_chars)
#     must_not_have_chars = not (re.fullmatch(r'(.)\1\1', string) or re.fullmatch(r'.*(.).*\1.*\1.*\1.*', string))
#     print(must_not_have_chars)
#     if len(string) < 12:
#         return False
#     elif must_have_chars and must_not_have_chars:
#         return True

# is_valid_password("Apfoajaz+4312948")

# Third try.
def is_valid_password(string):
    if len(string) < 12:
        return False

    contains_patterns = [r'[0-9]+', r'[a-z]+', r'[A-Z]+', r'[+\-*/.@]+']
    not_contains_patterns = [r'(.)\1\1', r'.*(.).*\1.*\1.*\1.*']

    for pattern in contains_patterns:
        if not re.search(pattern, string):
            print(pattern)
            return False
    for pattern in not_contains_patterns:
        if re.search(pattern, string):
            print(pattern)
            return False
    
    return True

# YAAAAAYYYYY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!