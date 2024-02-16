def digit_sum(n):
    sum = 0
    while len(str(n)) >= 2:
        sum += last_digit(n)
        n = remove_last_digit(n)
    sum += last_digit(n)
    return sum
def last_digit(n):
    return n % 10
def remove_last_digit(n):
    return n // 10

# print(148, remove_last_digit((1481)))
# print(1, last_digit(491))
# print(15, digit_sum(159))