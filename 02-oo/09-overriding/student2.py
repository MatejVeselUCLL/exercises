class Customer:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @staticmethod
    def can_be_sold_to(customer):
        return True
    
class AgeRestrictedItem(Item):
    @staticmethod
    def can_be_sold_to(customer):
        return customer.age >= 18
    
class CountryRestrictedItem(Item):
    @staticmethod
    def can_be_sold_to(customer):
        return customer.country != 'Arstotzka'

class ShoppingList:
    def __init__(self, owner):
        self.__owner = owner
        self.__items = []

    @property
    def owner(self):
        return self.__owner

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

    def add(self, item):
        if not item.can_be_sold_to(self.owner):
            raise ValueError()
        self.__items.append(item)

age = 0
country = 'Belgium'
expected = False
customer = Customer("John", age, country)
item = AgeRestrictedItem('tobacco', 15)
assert item.can_be_sold_to(customer) == expected