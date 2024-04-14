def indices_of(xs, condition):
    return [i for i, x in enumerate(xs) if condition(x)]

# def is_odd(x):
#     return x % 2 != 0

# print([0, 2, 4, 6], indices_of([1, 2, 3, 4, 5, 6, 7, 8], is_odd))
