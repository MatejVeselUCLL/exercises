# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen

# Time: 1h

import re
from abc import ABC, abstractmethod

class Person:
    def __init__(self, id, name, is_a_student):
        if not self.is_valid_name(name):
            raise ValueError()
        
        self.id = id
        self.__name = name # Q& there is redundancy in validation, is that OK?
        self.is_a_student = is_a_student

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not self.is_valid_name(name):
            raise ValueError()
        self.__name = name


    @staticmethod
    def is_valid_name(name):
        # A name must consist of at least two parts separated by a space.
        if re.fullmatch(r'[^\s]+\s[^\s]+.*', name):
            return True
        return False

# # person_with_invalid_name = Person(4, "Matej", True)
# person = Person(4, "Matej Vesel", True)
# person.name = "Hell O"

class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        # TODO
        self.__occupants = {} # This dictionary will use Person ids as keys and Person objects as values.

    @property # read-only
    def number_of___occupants(self):
        return len(self.__occupants)
    
    @property # read-only
    def maximum___occupants(self):
        # Each Person requires at least 20 square meters of space.
        # Each room can accommodate up to 2 people.
        # Example: area = 150 m^2, number_of_rooms = 7
        # 150 // 20 = 7
        # 7 * 2 = 14
        # min(7, 14) == 7 maximum___occupants
        
        return min(self.area // 20, self.number_of_rooms * 2)
    
    def register_resident(self, person):
        if person.id in self.__occupants.keys():  # TODO
            return
        elif self.number_of___occupants == self.maximum___occupants:
            raise RuntimeError()
        
        self.__occupants[person.id] = person

    def unregister_resident(self, id):
        self.__occupants.pop(id)
    
    @property
    def resident_names(self):
        return [person.name for person in self.__occupants.values()]
    
    @abstractmethod
    # Q& Is it ok if I add self?
    def calculate_value(self): # This method takes no parameters.
        ...


# residence = Residence("address", 150, 7)

class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self):
        return (25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity)
    
class StudentKot(Residence):
    def __init__(self, address, area):
        super().__init__(address, area, 1)

    # A Person must be a student in order to register in a StudentKot.
    def register_resident(self, person):
        if not person.is_a_student:
            raise RuntimeError
        super().register_resident(person)

    def calculate_value(self):
        return 150000 + (750 * self.area)


# # TESTING

# # create some people
# aimee = Person("12.34.56-789.01","Aimee Backiel",False)
# bastian = Person("01.02.03-040.05", "Bastian Li Backiel", True)

# # create some residences
# my_villa = Villa("Roeselbergdal 44, 3012 Wilsele", 151, 4, 1)
# my_kot = StudentKot("Kortestraat 6, 3000 Leuven",20)

# # check the values of the properties
# assert 427100, my_villa.calculate_value()
# assert 165000, my_kot.calculate_value()

# # move the people into a residence
# my_villa.register_resident(aimee)
# my_villa.register_resident(bastian)

# # check the residents of the villa
# assert ["Aimee Backiel","Bastian Li Backiel"], my_villa.resident_names

# # Someday, sadly Bastian will grow up and move into his student kot
# my_villa.unregister_resident(bastian.id)
# my_kot.register_resident(bastian)

# # check the residents again
# assert ["Aimee Backiel"], my_villa.resident_names
# assert ["Bastian Li Backiel"], my_kot.resident_names

# # With all her free time, Aimee can expand the garage to make space for all her hobbies
# my_villa.garage_capacity = 3
# assert 447100, my_villa.calculate_value()


# FILE: 10-exam-information\02-exam-2023\june-2023\01-housing\housing.py
# FIELD: __occupants
# SUPER CLASS: Residence
# THE ONLY INSTRUCTION: "Add another private field __occupants to store a dictionary of all the Persons registered at this Residence."
# PROBLEM: Private field of a super class is not seen from a child classes.

# # SIMPLIFIED PROBLEM CODE:
# class Animal(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

# class Beaver(Animal):
#     def __init__(self, name, age, fur_color):
#         super().__init__(name, age)
#         self.fur_color = fur_color
    
#     def get_age(self):
#         return super().__age

# john = Beaver("John", 5, "Dark brown")
# john.get_age() # AttributeError: 'super' object has no attribute '_Beaver__age'

