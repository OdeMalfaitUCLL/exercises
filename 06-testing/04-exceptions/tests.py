import pytest
from book import Book
@pytest.mark.parametrize('title', [
    ('Harry Potter'),
    ('Pluk en de Petteflet'),
    ('Warrior Cats')
    ])
@pytest.mark.parametrize('isbn', [
    ('978-9076174105'),
    ('978-9045110950'),
    ('978-94-6337-559-7')
])
def test_valid_creation(title,isbn):
    book = Book(title,isbn)
    assert book.title == title
    assert book.isbn == isbn
    
@pytest.mark.parametrize('isbn', [
    ('978-9076174105'),
    ('978-9045110950')
    ])
def test_creation_with_invalid_title(isbn):
    with pytest.raises(RuntimeError):
        Book('',isbn)

@pytest.mark.parametrize('title', [
    ('Harry Potter'),
    ('Pluk en de Petteflet'),
    ('Warrior Cats')
    ])
@pytest.mark.parametrize('isbn', [
    ('978-1779501126'),
    ('978-907617410555'),
    ('978')
    ])
def test_creation_with_invalid_isbn(title,isbn):
    with pytest.raises(RuntimeError):
        Book(title,isbn)