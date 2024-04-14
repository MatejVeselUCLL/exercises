class PadZip:
    def __init__(self, left, right, padding=None):
        self.__left = list(left)
        self.__right = list(right)
        self.__i = 0

        self.pad(padding)
    
    def pad(self, padding):
        if len(self.__left) == len(self.__right):
            pass
        elif len(self.__left) > len(self.__right):
            while len(self.__right) != len(self.__left):
                self.__right.append(padding)
        else:
            while len(self.__left) != len(self.__right):
                self.__left.append(padding)

    def __next__(self):
        if self.__i >= len(self.__left):
            raise StopIteration()
        
        current = (self.__left[self.__i], self.__right[self.__i])
        self.__i += 1
        return current

    def __iter__(self):
        return self

# print(list(PadZip('abcde', [1, 2, 3])))
# print(list(PadZip('abcde', [1, 2, 3], padding=0)))
# xs = PadZip('abc', 'xyz')
# print(list(xs))
# print(list(xs))