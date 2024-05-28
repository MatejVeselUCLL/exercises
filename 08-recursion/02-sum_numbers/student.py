def digit_at_index(int, i): #
    k = (len(str(int)) - 1) - i
    return (int // 10**k) % 10

# print(digit_at_index(234, 0), 2)
# print(digit_at_index(4835, 2), 3)

def sum_numbers(number):
    number = abs(number)
    k = len(str(number)) - 1
    if k == 0:
        return digit_at_index(number, 0)
    else:
        new_number = int(str(number)[:k])
        return sum_numbers(new_number) + digit_at_index(number, k)


# print(sum_numbers(234), 9)
# print(sum_numbers(123456789), 45)
# print(sum_numbers(-153), 9)

def sum_numbers(number):
    number = abs(number)
    k = len(str(number)) - 1
    if k == 0:
        return digit_at_index(number, 0)
    else:
        new_number = int(str(number)[-1])
        return sum_numbers(new_number) + int(str(number)[-1])