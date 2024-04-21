class Book:
    def __init__(self, title, isbn):
        if title == "":
            raise RuntimeError()
        self.__title = title

        isbn_copy =  [int(n) for n in isbn.replace(' ', '').replace('-', '')]
        if len(isbn_copy) != 13:
            raise RuntimeError()
        elif sum(isbn_copy[i] if i % 2 == 0 else isbn_copy[i]*3 for i in range(len(isbn_copy))) % 10 != 0:
            raise RuntimeError()
        self.__isbn = isbn
    
    # Q& is this a correct way to make readonly properties?

    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
        


# # Valid Book creation
# >>> book = Book('Watchmen', '978-1779501127')

# # Invalid title
# >>> book = Book('', '978-1779501127')
# RuntimeError

# # Invalid ISBN
# >>> book = Book('Watchmen', '978-1779501128')
# RuntimeError