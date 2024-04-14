def group_by(xs, key_function):
    grouped_xs = {}
    for x in xs:
        grouped_xs.setdefault(key_function(x), []).append(x)
    return grouped_xs

# def age(person):
#     return person.age

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# print(group_by([
#     Person(name='John', age=14),
#     Person(name='Marc', age=17),
#     Person(name='Sophie', age=15),
#     Person(name='Chris', age=17),
#     Person(name='Morgan', age=15),
# ], age))
# {
#     14: [Person(name='John', age=14)],
#     15: [Person(name='Sophie', age=15), Person(name='Morgan', age=15)],
#     17: [Person(name='Marc', age=17), Person(name='Chris', age=17)]
# }