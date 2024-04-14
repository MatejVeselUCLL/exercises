def fizzbuzz():
    n = 1
    while True:
        if (n % 3 == 0) and (n % 5 == 0):
            yield 'fizzbuzz'
        elif n % 3 == 0:
            yield 'fizz'
        elif n % 5 == 0:
            yield 'buzz'
        else:        
            yield str(n)
        n += 1

# import itertools
# print(list(itertools.islice(fizzbuzz(), 20)))
