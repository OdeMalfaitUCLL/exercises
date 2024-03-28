class Repeat:
    def __init__(self,number):
        self.__number = number
    def __iter__(self):
        return self
    def __next__(self):
        return self.__number