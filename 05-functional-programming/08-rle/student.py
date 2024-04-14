# class RleEncodeIterator:
#     def __init__(self, char):
#         self.__char = char
#         self.__count = 1

#     def __next__(self):
#         current = (self.__char, self.__count)
#         self.__count += 1
#         return current

#     def __iter__(self):
#         return self

#     @property
#     def char(self):
#         return self.__char

# def rle_encode(data):
#     encoded_data = []
#     rle_encode_iter = RleEncodeIterator(data[0])
#     for char in data[1:]:
#         if char == rle_encode_iter.char:
#             yield next(rle_encode_iter)
#         else:
#             encoded_data.append(next(rle_encode_iter))
#             rle_encode_iter = RleEncodeIterator(char)
#             next(rle_encode_iter)
#             yield encoded_data

# data = 'aaabbcccc'
# rle_encoder = rle_encode(data)
# print('(a, 1)', next(rle_encoder))
# print('(a, 2)', next(rle_encoder))
# print('(a, 3)', next(rle_encoder))
# print('(b, 1)', next(rle_encoder))
# print('(b, 2)', next(rle_encoder))
# print('(c, 1)', next(rle_encoder))
# print('(c, 2)', next(rle_encoder))
# print('(c, 3)', next(rle_encoder))
# print('(c, 4)', next(rle_encoder))

# data = 'aaabbcccc'
# rle_encoder = rle_encode(data)
# print("[('a', 3), ('b', 2), ('c', 4)]", , sep='\n')


# # print(rle_encode(data))
# # data = 'abcde'
# # print(rle_encode(data))


class RleEncodeIterator:
    def __init__(self, char):
        self.__char = char
        self.__count = 1

    def __next__(self):
        current = (self.__char, self.__count)
        self.__count += 1
        return current

    def __iter__(self):
        return self

    @property
    def char(self):
        return self.__char

def rle_encode(data):
    data = list(data)
    rle_encoder = RleEncodeIterator(None)  
    for char in data + [None]:
        if char == rle_encoder.char:
            next(rle_encoder)
        else:
            current = next(rle_encoder)
            rle_encoder = RleEncodeIterator(char)
            if current != (None, 1):
                yield current

# data = 'aaabbcccc'
# rle_encoder = rle_encode(data)
# print("[('a', 3), ('b', 2), ('c', 4)]", list(rle_encoder), sep="\n")

class RleDecodeIter:
    def __init__(self, pair):
        self.__char = pair[0]
        self.__count = pair[1]

    def __next__(self):
        if self.__count == 0:
            raise StopIteration
        self.__count -= 1
        return self.__char

    def __iter__(self):
        return self

def rle_decode(data):
    for pair in data:
        rle_decode_iter = RleDecodeIter(pair) 
        while True:
            try:
                yield next(rle_decode_iter)
            except StopIteration:
                break

# data = [('a', 3), ('b', 2), ('c', 4)]
# print(list(rle_decode(data)))
