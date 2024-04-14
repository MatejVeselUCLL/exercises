import re

def movie_count(movies, director):
    return len({
        movie.title
        for movie in movies
            if movie.director == director
    })

def longest_movie_runtime_with_actor(movies, actor):
    return max({
        movie.runtime
        for movie in movies
            if actor in movie.actors
    })

def has_director_made_genre(movies, director, genre):
    return any({
        True
        for movie in movies
            if movie.director == director
                for genree in movie.genres
                    if genree == genre
    })

def is_prime(n):
    if n in {0, 1}:
        return False
    return all({
        False
        for divisor in range(2, n)
            if (n % divisor) == 0
    })
# print(is_prime(4))

def is_increasing(ns):
    return all({
        ns[i+1] - ns[i] + 1 # plus one because of the 0, which is a falsey value.
        for i in range(len(ns)-1)
    })
# print(is_increasing([2, 1]))
# print(is_increasing([1, 1, 2, 3]))

def count_matching(xs, ys):
    return len([
        True
        for x, y in zip(xs, ys)
        if x == y
    ])
# print(count_matching(xs = ['a', 'b', 'c', 'd', 'e'], ys = [1]))

def weighted_sum(ns, weights):
    return sum([
        product * weight
        for product, weight in zip(ns, weights)
    ])

# def alternating_caps(string):
#     return "".join([
#         f"{odd.upper()}{even.lower()}"
#         for odd, even in zip(list(string[::2]), (list(string[1::2]) + [""]))
#     ])

def alternating_caps(string):
    return "".join([
        char.upper() if (i % 2) == 0 else char.lower()
        for i, char in enumerate(list(string))
    ])

# def find_repeated_words(sentence):
#     match = re.match(r'(\b\w+\b)[^\w]+\1', sentence)
#     if match is None:
#         return set()
#     return set(match.groups())

def find_repeated_words(sentence):
    return set(re.findall(r'(\b\w+\b)[^\w]+\1', sentence.lower()))

# print(find_repeated_words("This sentence has has repeated words. Words."))
# print(find_repeated_words("This sentence has"))