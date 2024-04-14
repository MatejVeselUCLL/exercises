
class InclusiveRange:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __iter__(self):
        return InclusiveRangeIterator(self.__a, self.__b)

class InclusiveRangeIterator:
    def __init__(self, a, b):
        self.__b = b
        self.current = a

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current

        if self.__a <= self.__b:
            if current == self.__b + 1:
                raise StopIteration()
            self.current += 1
        else:
            raise StopIteration()
        
        return current

# for i in InclusiveRange(-5, -5):
#     print(i)

# for i in InclusiveRange(-4, -5):
#     print(i)

# for i in InclusiveRange(-3, -5):
#     print(i)

# for i in InclusiveRange(1, 5):
#     print(i)

# r = InclusiveRange(1, 5)
# print(list(r))
# print(list(r))

# iterator = iter(r)
# print(list(iterator))
# print(list(iterator))