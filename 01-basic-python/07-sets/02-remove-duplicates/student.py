# def remove_duplicates(xs):
#     xs_copy = xs.copy()
#     for i in range(len(xs_copy)):
#         for j in range(len(xs_copy) -1, i, -1):
#             if xs_copy[i] == xs_copy[j]:
#                 xs_copy.pop(j)
#     return xs_copy

# def remove_duplicates(xs):
#     xs_copy = xs.copy()
#     for i in range(len(xs_copy) - 1, -1, -1):
#         if xs_copy[i] in set(xs_copy[i-1:-1:-1]):
#             xs_copy.pop(i)
#     return xs_copy


print([4, 3, 2, 1, 5], remove_duplicates([4, 3, 4, 2, 2, 1, 5]))

# [4, 3, 4, 2, 2, 1, 5]
# (1, 2, 3, 4, 5)
# [4, 3, 2, 1, 5]

# [4, 3, 4, 2, 2, 1, 5]
# [4, 3, 4, 2, 2, 1, 5]
# (1, 2, 3, 4, 5)
