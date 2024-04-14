def merge_dictionaries(d1, d2, merge_function):
    merged_dict = {}
    for k in d1:
        if k in d2:
            merged_dict[k] = merge_function(d1[k], d2[k])
        else:
            merged_dict[k] = d1[k]
    for k in d2:
        if k not in d1:
            merged_dict[k] = d2[k]
    return merged_dict

# def merge_function(a, b):
#     return a+b

# d1 = {"Matej": 20, "Nejc": 5}
# d2 = {"Natasa": 47, "Matej": 20}
# print({"Matej": 40, "Nejc": 5, "Natasa": 47}, merge_dictionaries(d1, d2, merge_function))