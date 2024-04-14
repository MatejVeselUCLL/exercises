# def find_first_book_by_author(books, author):
#     for book in books:
#         if book.author == author:
#             return book
#     return None

# def condition(object, field_value):
#     return object.author == field_value

def find(iterable, condition):
    for element in iterable:
        if condition(element):
            return element
    return None