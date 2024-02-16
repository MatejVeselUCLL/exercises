def is_increasing(ns):
    ms = ns[1:]
    paired = list(zip(ns, ms))
    for first, second in paired:
        if first > second:
            return False
    return True

# print(True, is_increasing([1, 2, 3, 4, 4, 7]))
# print(False, is_increasing([1, 3, 2, 4]))

# [1, 2, 3]
# [2, 3]
# [(1, 2), (2, 3)]

