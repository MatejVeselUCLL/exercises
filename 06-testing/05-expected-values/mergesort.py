from math import ceil

def split_in_two(ns):
    i = ceil(len(ns) / 2 - 0.5)
    return (ns[:i], ns[i:])

# print(split_in_two([1, 2, 3, 4, 5, 6]))
# print(split_in_two([1, 2, 3, 4, 5, 6, 7]))

def merge_sorted(left, right):
    if len(left) == 0 or len(right) == 0:
        return left + right
    
    il = iter(left)
    ir = iter(right)
    current_left = next(il)
    current_right = next(ir)
    il_end = 0
    ir_end = 0
    result = []
    
    for i in range(len(left) + len(right)): # Number of elements end result list.
        if current_left < current_right:
            result.append(current_left)
            try:
                current_left = next(il)
            except StopIteration:
                result.append(current_right)
                result += list(ir)
                return result
            
        elif current_right < current_left:
            result.append(current_right)
            try:
                current_right = next(ir)
            except StopIteration:
                result.append(current_left)
                result += list(il)
                return result

        else:
            result.append(current_left)
            result.append(current_right)
            try:
                current_left = next(il)
            except StopIteration:
                try:
                    current_right = next(ir)
                except StopIteration:
                    result += list(ir)
                    return result
                result.append(current_right)
                result += list(ir)
                return result
            try:
                current_right = next(ir)
            except StopIteration:
                result.append(current_left)
                result += list(il)
                return result

# print(merge_sorted([1, 2], [0,1]))
# print(merge_sorted([1], [1, 2, 3, 4, 5, 6]))

# Copies from solutions. We've not seen recursive functions before.
def merge_sort(ns):
    if len(ns) <= 1:
        return ns
    left, right = split_in_two(ns)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge_sorted(sorted_left, sorted_right)
    
# print(merge_sort([3, 5, 2]))
