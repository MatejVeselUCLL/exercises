# def rotate(xs, n):
#     xs = xs[n:] + xs[:n]

def rotate(xs, n):
    for i in range(n):
        xs.append(xs[0])
        xs.pop(0)

xs = [1, 2, 3, 4, 5]
rotate(xs, 2)
print([3, 4, 5, 1, 2], xs)
xs = [1, 2, 3, 4, 5]
rotate(xs, 1)
print([2, 3, 4, 5, 1], xs)

# Q&A This code does nothing? Why?