from itertools import permutations, pairwise
def find_shortest_path(distance, city_count):
    return min((path for path in [[0, *p, 0] for p in permutations(range(1, city_count))]), key=lambda path,distance:sum(distance(a, b) for a, b in pairwise(path)))

    def total_distance(path, f=distance):
        return sum(distance(a, b) for a, b in pairwise(path))
    paths = [[0, *p, 0] for p in permutations(range(1, city_count))]
    return min((path for path in paths), key=total_distance)


# def find_shortest_path(distance, city_count):
#     # distance_and_path = {(total_distance(path): pr)}
#     # # distance_and_path = {distance: path for path in list(pr)}

#     pr = permutations(range(1, city_count))
#     paths = []
#     for permutation in list(pr):
#         path = list(permutation)
#         path = [0, *path, 0]
#         paths.append(path)
    
#     distance_and_path = {}
#     for path in paths:
#         distance_and_path[total_distance(path, distance)] = path
    
#     return distance_and_path[min(distance_and_path.keys())]

# def total_distance(path, distance):
#     pw = pairwise(path)
#     return sum(distance(a, b) for a, b in pw)

    


