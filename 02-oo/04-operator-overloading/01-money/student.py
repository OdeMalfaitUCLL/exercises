class Money:
    def __init__(self,amount, currency):
        self.amount = amount
        self.currency = currency
    def __add__(self,other):
        if not isinstance(other,Money):
            raise TypeError("ander type kan je niet optellen")
        else:
            if self.currency == other.currency:
                return Money(self.amount + other.amount, self.currency)
            else: raise RuntimeError("Mismatched currencies!")
    def __sub__(self,other):
        if not isinstance(other,Money):
            raise TypeError("ander type kan je niet van elkaar aftrekken")
        else:
            if self.currency == other.currency:
                return Money(self.amount - other.amount, self.currency)
            else: raise RuntimeError("Mismatched currencies!")
    def __mul__(self,factor):
        return Money(self.amount * factor, self.currency)

money1 = Money(10, "EUR")
money2 = Money(20, "EUR")
add = money1 + money2
print(add.amount)
min = money2-money1
print(min.amount)
print(Money(20, "EUR") * 5)