def cycle(xs):
    # i = 0
    # while 1:
    #     yield xs[i]
    #     i += 1
    #     if i == len(xs):
    #         i = 0

    while 1:
        for element in xs:
            yield element
        

# import itertools
# xs = cycle('abcd')
# print(list(itertools.islice(xs, 10)))  # Take 10 first elements