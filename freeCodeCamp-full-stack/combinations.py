# Counting Cards
# A standard deck of playing cards has 13 unique cards in each suit.
# Given an integer representing the number of cards to pick from the deck,
# return the number of unique combinations of cards you can pick.
#
# Order does not matter. Picking card A then card B is the same as picking card B then card A.
# For example, given 52, return 1. There's only one combination of 52 cards to pick from a 52 card deck.
# And given 2, return 1326, There's 1326 card combinations you can end up with when picking 2 cards from the deck.

def combinations(cards):
    cards_in_deck = 52
    numerator = 1
    denominator = 1
    for i in range(cards_in_deck, cards_in_deck - cards, -1):
        numerator *= i
    for i in range(cards, 0, -1):
        denominator *= i
    combinations_count = numerator / denominator
    return combinations_count


assert (combinations(52) == 1)
assert (combinations(1) == 52)
assert (combinations(2) == 1326)
assert (combinations(5) == 2598960)
assert (combinations(10) == 15820024220)
assert (combinations(50) == 1326)
