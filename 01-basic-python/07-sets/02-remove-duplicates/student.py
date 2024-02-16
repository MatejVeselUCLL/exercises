def remove_duplicates(xs):
    xs_copy = []
    xs_set = set(xs)
    for item in xs:
        if item in xs_set:
            xs_copy.append(item)
            xs_set.remove(item)
    return xs_copy


# print([4, 3, 2, 1, 5], remove_duplicates([4, 3, 4, 2, 2, 1, 5]))

# [4, 3, 4, 2, 2, 1, 5]
# [4, 3, 4, 2, 2, 1, 5]
# (1, 2, 3, 4, 5)
# [4, 3, 2, 1, 5]
