# EXPERIMENT
# xs = [1, 2, 3]
# ys = ['a', 'b', 'c', 'd']

# print(list(zip(xs, ys)))
# # [(1, 'a'), (2, 'b'), (3, 'c')]

def add_indices(xs):
    return list(zip(range(len(xs)), xs))

# print("[(0, 'a'), (1, 'b'), (2, 'c')]\n", add_indices(['a', 'b', 'c']))
