def target_sum(ns, target):
    for i in range(len(ns)):
        for j in range(len(ns)-1, -1+i, -1):
            if ns[i] + ns[j] == target:
                return True
    return False

# 1 + 1
# 1 + 2
# 1 + 3
# 2 + 2
# 2 + 3
# 3 + 3


# print(True, target_sum([1, 2, 3], 5))
# print(False, target_sum([1, 2, 3], 7))
# print(True, target_sum([1, 2, 3], 6))