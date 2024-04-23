

import itertools


class Book:
    def __init__(self,title,isbn):
        if not Book.isValidTitle(title):
            raise RuntimeError("Invalid Title")
        if not Book.isValidIsbn(isbn):
            raise RuntimeError("Invalid isbn")
        self.__title = title
        self.__isbn = isbn
    
    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    @staticmethod
    def isValidTitle(title):
        return len(title) > 0
    @staticmethod
    def isValidIsbn(isbn):
        digits = [int(x) for x in isbn if x.isnumeric()]
        if len(digits) != 13:
            return False
        sum_digits = sum(y*weight for y, weight in zip(digits,itertools.cycle([1,3])))
        return sum_digits % 10 == 0