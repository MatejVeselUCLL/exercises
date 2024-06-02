class CircularBuffer:
    def __init__(self, n):
        self.buffer = []
        self.max_len = n
    
    def add(self, item):
        if len(self.buffer) == self.max_len:
            self.buffer.pop(0)
        self.buffer.append(item)
    
    def __getitem__(self, index):
        return self.buffer[index]

    def __len__(self):
        return len(self.buffer)
        
        



buffer = CircularBuffer(3)
print(0, len(buffer))
buffer.add('a')
buffer.add('b')
buffer.add('c')
print(3, len(buffer))
print('a', buffer[0])
print('b', buffer[1])
print('c', buffer[2])
buffer.add('d')
print(3, len(buffer))
print(['b', 'c', 'd'], [buffer[0], buffer[1], buffer[2]])