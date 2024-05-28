def reverse_from_right(text):
    k = len(text) - 1
    if k == 0:
        return text[0]
    else:
        return text[k] + reverse_from_right(text[:k])

def reverse_from_left(text):
    k = len(text) - 1
    if k == 0:
        return text[-1]
    else:
        return reverse_from_left(text[1:]) + text[-k-1]

# print(reverse_from_right('abcd'), 'dcba')
# print(reverse_from_left('abcd'), 'dcba')