from util import Card

def genres(movies):
    return {
        genre
        for movie in movies
        for genre in movie.genres
        # *movie.genres for movie in movies
    }

def actors(movies):
    return {
        actor
        for movie in movies
        for actor in movie.actors
    }

def repeat_consecutive(xs, n):
    return [
        element
        for element in xs
        for i in range(n)
    ]

# print(repeat_consecutive([1, 2, 3], 4), [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3])

def repeat_alternating(xs, n):
    return [
        element
        for i in range(n)
            for element in xs
    ]

# print(repeat_alternating([1, 2, 3], 4), [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

def cards(values, suits):
    return {
        Card(value, suit)
        for suit in suits
            for value in values
    }

# print(cards([2, 5, 10], ['hearts', 'diamonds']), {Card(2, 'hearts'), Card(5, 'hearts'), Card(10, 'hearts'), Card(2, 'diamonds'), Card(5, 'diamonds'), Card(10, 'diamonds')})