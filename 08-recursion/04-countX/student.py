def is_x(char):
    return 1 if char == 'x' else 0

def countX(text):
    k = len(text) - 1
    if k == 0:
        return is_x(text[0])
    elif text == "":
        return 0
    else:
        return countX(text[:k]) + is_x(text[k])

# print(countX('axpxc'), 2)
# print(countX('xxxx'), 4)
# print(countX(""), 0)
    
