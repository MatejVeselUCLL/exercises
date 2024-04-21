import pytest
from book import Book

@pytest.mark.parametrize('title, isbn', [
    ("Amroh Kuli", "978-0-439-02348-1"),
    ("Leaf of Retention", "979-8-886-45174-0"),
    ("Broad Web", "979-8-886-45174-0"),
    ("Teenager Guide", "979-8-886-45174-0"),
    ("Villains of the Dark","979-8-886-45174-0")
])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    assert book.title == title, f"title: {title}, expected True, received False."
    assert book.isbn == isbn, f"isbn: {isbn}, expected True, received False."

@pytest.mark.parametrize('invalid_title', [
    (''),
    (' '),
    ('  3 ')
])
def test_creation_with_invalid_title(invalid_title):
    with pytest.raises(RuntimeError):
        Book(invalid_title,"289284528-9")

@pytest.mark.parametrize('invalid_isbn', [
    ("4314341510-5"),
    ("4314341510-31232345"),
    ("4314"),
    ("")
])
def test_creation_with_invalid_isbn(invalid_isbn):
    with pytest.raises(RuntimeError):
        Book("Broad Web", invalid_isbn)