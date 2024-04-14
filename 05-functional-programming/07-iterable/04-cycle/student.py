class Cycle:
    def __init__(self, x):
        self.__x = x
        self.__i = 0
    
    def __next__(self):
        current = self.__x[self.__i]
        self.__i += 1
        if self.__i == len(self.__x):
            self.__i = 0
        return current

    def __iter__(self):
        return self


# import itertools
# xs = Cycle('abcd')
# print(list(itertools.islice(xs, 10)))  # Take 10 first elements