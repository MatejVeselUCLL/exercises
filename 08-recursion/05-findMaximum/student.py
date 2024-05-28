def is_greater_than(a, b):
    return a if a > b else b

def findMaximum(list):  
    k = len(list) - 1
    if k == 0:
        return list[0]
    else:
        return is_greater_than(list[k], findMaximum(list[:k]))

# print(findMaximum([3, 5, 1, 7]), 7)
# print(findMaximum([7, 4, 1]), 7)
# # print(findMaximum([])) IndexError