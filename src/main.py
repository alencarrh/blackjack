# -*- coding: utf-8 -*-
from src.classes import Deck

deck = Deck()


def print_deck(deck: Deck):
    brank_in = 5
    i = 1
    for card in deck.cards:
        print(card, end="\n" if i % brank_in == 0 else ", ")
        i += 1
    print()


print_deck(deck)

deck.shuffle()
print("\n\nThe deck was shuffled\n\n")

print_deck(deck)

deck.cut(30)  # there are 52 cards

print("\n\nThe deck was cut\n\n")

print_deck(deck)

print("\n\n")
print(deck.get_card())
print(deck.get_card())
print(deck.get_card())
print(deck.get_card())
