def coins(one, two, five, goal):
    for one_coefficient in range(one+1):
        for two_coefficient in range(two+1):
            for five_coefficient in range(five+1):
                if one_coefficient*1 + two_coefficient*2 + five_coefficient*5 == goal:
                    return True
    return False

# print(True, coins(1, 1, 1, 6))
# print(True, coins(1, 1, 1, 8))
# print(False, coins(1, 1, 1, 4))