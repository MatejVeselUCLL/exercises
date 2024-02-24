class Queue:
    def __init__(self):
        self.__items = []
    def add(self, item):
        self.__items.append(item)
    def next(self):
        return self.__items.pop(0)
    def is_empty(self):
        return not self.__items
    
# queue = Queue()
# print(True, queue.is_empty())

# queue.add('john')
# print(True, not queue.is_empty())

# print(True, queue.next() == 'john')
# print(True, queue.is_empty())

# queue.add('a')
# queue.add('b')
# queue.add('c')
# print(True, queue.next() == 'a')