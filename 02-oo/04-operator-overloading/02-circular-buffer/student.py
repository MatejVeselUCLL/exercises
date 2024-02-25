class CircularBuffer:
    def __init__(self, max_length):
        self.max_length = max_length
        self.buffer = []
    
    def add(self, item):
        if len(self.buffer) == self.max_length:
            self.buffer.pop(0)
        self.buffer.append(item)
    
    def __getitem__(self, i):
        return self.buffer[i]
    
    def __len__(self):
        return len(self.buffer)


# Q& Why are all dunder methods not shown in VSCode when typing?