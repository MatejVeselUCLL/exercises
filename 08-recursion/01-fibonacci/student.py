def fibonacci(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
    
# The method is inefficient, because it is recursive, and it has to calculate all fibonacci numbers before 'number' also. It is not a single formula, but a loop.

# print(fibonacci(0), 0)
# print(fibonacci(3), 2)
# print(fibonacci(-5), 0)