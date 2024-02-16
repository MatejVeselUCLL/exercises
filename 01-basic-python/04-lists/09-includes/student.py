def includes(xs, ys):
    return set(xs).issuperset(set(ys))

print(True, includes([1, 2, 3], [1, 2]))
print(False, includes([1, 2, 3], [1, 2, 4]))
print(True, includes([1, 2, 3], [1, 1, 1, 1, 1]))