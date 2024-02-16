def target_sum(ns, target):
    for i in range(len(ns)):
        for j in range(len(ns)-1, 0+i, -1):
            if ns[i] + ns[j] == target:
                return True
    return False