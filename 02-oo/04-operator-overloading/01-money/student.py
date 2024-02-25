class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def check_currencies(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")

    def __add__(self, other):
        self.check_currencies(other)
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        self.check_currencies(other)
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, num):
        return Money(self.amount * num, self.currency)


# money = Money(10, 'EUR')
# print(10, money.amount)
# print('EUR', money.currency)
# print("Money(30, 'EUR')", Money(10, 'EUR') + Money(20, 'EUR'))
# print("RuntimeError('Mismatched currencies!')", Money(10, 'EUR') + Money(20, "USD"))
# print("Money(20, 'EUR')", Money(30, 'EUR') - Money(10, 'EUR'))
# print("RuntimeError('Mismatched currencies!')", Money(30, 'EUR') - Money(10, "USD"))
# print("Money(100, 'EUR')", Money(20, 'EUR') * 5)