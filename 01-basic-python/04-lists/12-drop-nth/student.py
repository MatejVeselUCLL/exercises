def drop_nth(xs, n):
    xs_copy = xs.copy()
    del xs_copy[n]
    return xs_copy