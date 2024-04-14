from util import *

def group_by_suit(cards):
    return group_by(cards, lambda card: card.suit)

def group_by_value(cards):
    return group_by(cards, lambda card: card.value)

def partition_by_color(cards):
    return partition(cards, lambda card: card.suit in ['spades', 'clubs'])

# cards = [Card(2, 'hearts'), Card(3, 'hearts'), Card(2, 'spades'), Card(9, 'hearts'), Card(2, 'diamonds')]
# print("By suit:\t", group_by_suit(cards))
# print("By value:\t", group_by_value(cards))
# print("Partition by color:\t", partition_by_color(cards))