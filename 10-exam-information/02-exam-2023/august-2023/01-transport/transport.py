# enter your code here to solve the transporation assignment
# voer hier je code in om de vervoersvraag op te lossen

import re
from abc import ABC, abstractmethod

class Passenger:
    def __init__(self, id, name, money):
        if not self.is_valid_name(name):
            raise ValueError()
        
        self.id = id
        self.money = money
        self.__name = name

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
        if re.fullmatch(r'[^\s]+\s[^\s]+.*', name):
            return True
        return False

class Vehicle(ABC):
    def __init__(self, license_plate, amount_of_seats):
        self.license_plate = license_plate
        self.amount_of_seats = amount_of_seats
        self.__occupants = {} # This dictionary will use Passenger ids as keys and Passenger objects as values.

    @property
    def number_of_occupants(self):
        return len(self.__occupants)

    @property
    @abstractmethod
    def maximum_occupants():
        ...

    def add_passenger(self, passenger):
        self.__occupants[passenger.id] = passenger

    def remove_passenger(self, passenger):
        self.__occupants.pop(passenger.id)

    def remove_all_passengers(self):
        self.__occupants = {}

    @property
    def occupant_names(self):
        return [person.name for person in self.__occupants.values()]
    
class Taxi(Vehicle):
    def __init__(self, license_plate, amount_of_seats):
        super().__init__(license_plate, amount_of_seats)
        self.is_available = True

    @property
    def maximum_occupants(self):
        return self.amount_of_seats
    
    def pickup(self, passengers, distance):
        if (not self.is_available) or (len(passengers) > self.maximum_occupants):
            raise ValueError()
        
        # Calculate fare: 1 + distance; there is a minimum fare of 5 euros.
        fare = 1 + distance
        if fare < 5:
            fare = 5
        
        # The first Passenger in the passengers list is responsible to pay for the ride.
        payer = passengers[0]
        if payer.money < fare:
            raise RuntimeError()
        payer.money -= fare

        # All Passengers in the passengers list should be registered as riding in this Taxi.
        for passenger in passengers:
            self.add_passenger(passenger)

        self.is_available = False
    
    def dropoff(self):
        self.remove_all_passengers()
        self.is_available = True

class Bus(Vehicle):
    # Constructor is inherited. Q& OK?

    @property
    def maximum_occupants(self):
        return 2 * self.amount_of_seats
    
    def board(self, passenger):
        if 1 + self.number_of_occupants > self.maximum_occupants:
            raise RuntimeError()

        fare = 2
        if passenger.money < fare:
            raise RuntimeError()
        passenger.money -= fare

        self.add_passenger(passenger)

    def disembark(self, passenger):
        self.remove_passenger(passenger)


# TESTING

# # create some passengers
# aimee = Passenger("12.34.56-789.01", "Aimee Backiel", 40)
# bastian = Passenger("01.02.03-040.05", "Bastian Li Backiel", 5)

# # create some vehicles
# my_taxi = Taxi("1-NGL-760", 4)
# my_bus = Bus("1-HUE-344", 30)

# # taking a bus ride together; Bastian likes to pay for himself
# my_bus.board(aimee)
# my_bus.board(bastian)

# # check the occupants of the bus
# print(["Aimee Backiel", "Bastian Li Backiel"], my_bus.occupant_names)

# # they get off at the zoo
# my_bus.disembark(aimee)
# my_bus.disembark(bastian)

# # check the occupants again
# print([], my_bus.occupant_names)

# # Bastian wants to take the bus alone for the first time, and Aimee follows him in a taxi
# # they only ride 5 km to be sure he doesn't get lost
# my_bus.board(bastian)
# my_taxi.pickup([aimee],5)

# # check the occupants in each vehicle
# print(["Bastian Li Backiel"], my_bus.occupant_names)
# print(["Aimee Backiel"], my_taxi.occupant_names)

# # check how much money remains in their wallets
# print(32, aimee.money)
# print(1, bastian.money)