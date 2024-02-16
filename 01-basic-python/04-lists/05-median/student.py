import math
def median(ns):
    ns.sort()
    middle_index = (len(ns) - 1) / 2
    if len(ns) % 2 != 0: # odd
        return ns[int(middle_index)]
    else:
        first = ns[math.ceil(middle_index)]
        second = ns[math.floor(middle_index)]
        average = (first + second) / 2
        return average

# print(3, median([1,2,3,4,5]))
# print(2.5, median([1,2,3,4]))
# print(3, median([1, 3, 2]))