def sort_by_age(people):
    return sorted(people, key=lambda person: person.age)

def sort_by_decreasing_age(people):
    return sorted(people, key=lambda person: -person.age)

def sort_by_name(people):
    return sorted(people, key=lambda person: person.name)

def sort_by_name_then_age(people):
    return sorted(people, key=lambda person: (person.name, person.age))

def sort_by_name_then_decreasing_age(people):
    return sorted(people, key=lambda person: (person.name, -person.age))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"({self.name}, {self.age})"

people = [Person("Matej", 20), Person("Nejc", 5), Person("Nataša", 50), Person("Bojan", 60), Person("Nataša", 60)]

print("By age:\t\t", sort_by_age(people))
print("By decreasing age:\t\t", sort_by_decreasing_age(people))
print("By name:\t\t", sort_by_name(people))
print("By name, then age:\t\t", sort_by_name_then_age(people))
print("By name, then decreasing age:\t\t", sort_by_name_then_decreasing_age(people))