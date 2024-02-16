def rotate(xs, n):
    xs = xs[n:] + xs[:n]

# xs = [1, 2, 3, 4, 5]
# rotate(xs, 2)
# print([3, 4, 5, 1, 2], xs)
# xs = [1, 2, 3, 4, 5]
# rotate(xs, 1)
# print([2, 3, 4, 5, 1], xs)

# Q&A This code does nothing? Why?