from util import group_by, partition
def group_by_suits(cards):
    return group_by(cards, lambda card: card.suit)
def group_by_values(cards):
    return group_by(cards, lambda card: card.value)
def partition_by_color(cards):
    return partition(cards, lambda card : card.suit in ["spades" , "clubs"])