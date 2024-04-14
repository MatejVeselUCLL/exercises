class Repeat:
    def __init__(self, x):
        self.x = x
    
    def __next__(self):
        return self.x

    def __iter__(self):
        return self

# xs = Repeat(5)
# print(next(xs))
# print(next(xs))
# print(next(xs))