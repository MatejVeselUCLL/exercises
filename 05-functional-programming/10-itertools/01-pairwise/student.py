from itertools import pairwise

def total_distance(path, distance):
    pw = pairwise(path)
    return sum(distance(a, b) for a, b in pw)
