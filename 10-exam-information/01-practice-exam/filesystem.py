# Enter your code here: SKY IS NOT THE LIMIT.

# Time: 1h 20'

from abc import ABC, abstractmethod
import re
class StorageDevice:
    def __init__(self, block_count, block_size):
        self.__available_blocks = {i for i in range(block_count)}
        self.__used_blocks = set()
        self.__block_size = block_size
    
    @property
    def available_block_count(self):
        return len(self.__available_blocks)
    
    @property
    def used_block_count(self):
        return len(self.__used_blocks)
    
    @property
    def total_block_count(self):
        return self.available_block_count + self.used_block_count
    
    @property
    def block_size(self):
        return self.__block_size
    
    def allocate(self, block_count):
        blocks = []
        for i in range(block_count):
            if len(self.__available_blocks) == 0:
                raise RuntimeError()
            blocks.append(self.__available_blocks.pop())
            self.__used_blocks.add(blocks[-1])
        return blocks
        
    def free(self, blocks): # Block is a list of block indices.
        for block in blocks:
            if block not in self.__used_blocks:
                raise RuntimeError()
            self.__used_blocks.remove(block)
            self.__available_blocks.add(block)

class Entity(ABC):
    def __init__(self, storage, name):
        if not self.is_valid_name(name):
            raise RuntimeError()
        
        self.__storage = storage
        self.__name = name

    @staticmethod
    def is_valid_name(name):
        if re.match(r'^[a-zA-Z0-9.]{1,16}$', name):
            return True
        return False
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if not self.is_valid_name(name):
            raise RuntimeError()
        self.__name = name

    @property
    def storage(self):
        return self.__storage

    @property
    @abstractmethod
    def size_in_blocks(self):
        ...

    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.storage.block_size
    
    @abstractmethod
    def clear(self):
        ...


class File(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__occupied_blocks = []
    # Q& Do we have to define the construtor, if it's the same as super's constructor?

    # A freshly created File is empty and therefore occupies zero blocks of storage.

    # Define a method grow(block_count) which allocates an extra block_count blocks from its storage. These extra blocks must also be kept track of.
    def grow(self, block_count):
        new_occupied_blocks = self.storage.allocate(block_count)
        self.__occupied_blocks += new_occupied_blocks
        return new_occupied_blocks
    
    @property
    def size_in_blocks(self):
        return len(self.__occupied_blocks)
    
    def clear(self):
        self.storage.free(self.__occupied_blocks)
        self.__occupied_blocks = []


class Directory(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.children = []
    
    def add(self, entity):
        self.children.append(entity)
    
    @property 
    def size_in_blocks(self):
        # The size of a Directory is defined as the sum of the sizes of all its children.
        return sum(child.size_in_blocks for child in self.children)
    
    # Define a method clear() that clears all files recursively.
    def clear(self):
        for child in self.children:
            child.clear()





# # TESTING Directory

# my_ssd = StorageDevice(block_count=1000, block_size=4096)
# directory = Directory(storage=my_ssd, name='myfolder')

# # Initially, a directory takes no room
# print(0, directory.size_in_blocks)

# # We add a file
# file1 = File(my_ssd, 'file1')
# file1.grow(5)
# directory.add(file1)

# # The directory's size is the sum of all of its children's sizes
# print(5, directory.size_in_blocks)

# # We add a second file
# file2 = File(my_ssd, 'file2')
# file2.grow(10)
# directory.add(file2)
# print(15, directory.size_in_blocks)

# # We create a subdirectory and add a file to it
# subdir = Directory(my_ssd, 'subdir')
# directory.add(subdir)
# file3 = File(my_ssd, 'file3')
# file3.grow(20)
# subdir.add(file3)

# # The directory's size has grown
# print(35, directory.size_in_blocks)

# # All files are cleared recursively
# directory.clear()
# print(0, directory.size_in_blocks)
# print(0, file1.size_in_blocks)
# print(0, file2.size_in_blocks)
# print(0, file3.size_in_blocks)


# # TESTING File

# storage = StorageDevice(block_count=10, block_size=4096)

# # Create a file named 'filename.txt'
# file = File(storage=storage, name='filename.txt')


# # Getting file's name
# print('filename.txt', file.name)


# # Changing file's name
# file.name = 'newname.txt'
# print('newname.txt', file.name)


# # Trying to set an invalid name
# # print(RuntimeError, file.name = 'invalid name')


# # We allocate 8 blocks of storage for this file
# file.grow(block_count=8)

# # Getting the size in blocks
# print(8, file.size_in_blocks)

# # Storage has 8 fewer blocks available
# print(2, storage.available_block_count)
# print(8, storage.used_block_count)

# # Computing its size in bytes (= number of blocks used * block_size of storage)
# print(32768, file.size_in_bytes)

# # Clearing file resets its size to 0
# file.clear()
# print(0, file.size_in_blocks)

# # Storage has been freed
# print(10, storage.available_block_count)
# print(0, storage.used_block_count)

# # TESTING Entity
# print(True, Entity.is_valid_name(".asdfjkl2"))
# print(False, Entity.is_valid_name(" "))
# print(False, Entity.is_valid_name("asjkldaafjklfjkldfjklsdf"))


# # TESTING StorageDevice

# storage = StorageDevice(block_count=10, block_size=5)
# # available blocks: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # used blocks: []

# print(5, storage.block_size)
# print(10, storage.total_block_count)
# # Initially, all blocks are available...
# print(10, storage.available_block_count)
# # ...and no blocks are in use
# print(0, storage.used_block_count)

# storage = StorageDevice(block_count=10, block_size=5)
# # available blocks: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # used blocks: []

# print([0, 1, 2], storage.allocate(3))
# # available blocks: [3, 4, 5, 6, 7, 8, 9]
# # used blocks: [0, 1, 2]
# print([3, 4, 5, 6, 7], storage.allocate(5))
# # available blocks: [8, 9]
# # used blocks: [0, 1, 2, 3, 4, 5, 6, 7]
# storage.free([2, 3, 4])
# # available blocks: [2, 3, 4, 8, 9]
# # used blocks: [0, 1, 5, 6, 7]
# # Cannot free blocks that are not in use
# # print(RuntimeError, storage.free([9]))

