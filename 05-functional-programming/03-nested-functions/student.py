# def count_older_than(people, min_age):
#     return len([0 for person in people if person.age >= min_age])

# def indices_of_cards_with_suit(cards, suit):
#     return [i for i, card in enumerate(cards) if card.suit == suit]

def count_older_than(people, min_age):
    def older_than(person, min_age):
        return person.age >= min_age
        
    return len([0 for person in people if older_than(person, min_age)])


def indices_of_cards_with_suit(cards, suit):
    def matches_suit(card, suit):
        return card.suit == suit

    return [i for i, card in enumerate(cards) if matches_suit(card, suit)]

"Finished '01-comprehensions', '02-higher-order-functions' and '03-nested-functions' in chapter '05-functional-programming'"