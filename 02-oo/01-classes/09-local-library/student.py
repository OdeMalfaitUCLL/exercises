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
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                self.books.remove(book)

    def search_books(self, search_string):
        search_list = []
        for b in self.books:
            if (search_string.lower() in b.title.lower() or search_string.lower() in b.author.lower()):
                search_list.append(b)
        return search_list

hp = Book('hp', 'jkr')
bertem = Library('Bertem')
bertem.add_book(hp)
print(bertem.search_books('hp'))