class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_books(self, search_string):
        matching_books = []
        for book in self.books:
            matching_title = search_string.lower() in book.title.lower()
            matching_author = search_string.lower() in book.author.lower()
            if matching_title or matching_author:
                matching_books.append(book)
        return matching_books
