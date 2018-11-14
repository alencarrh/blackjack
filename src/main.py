# -*- coding: utf-8 -*-
from random import randint

from src.classes import Deck, Hand

deck = Deck(1)
deck.shuffle()
deck.cut(randint(1, deck.cards_left() - deck.cards_left() / 4))

user_hand = Hand()

user_hand.add_card(deck.pop_card())
print(user_hand)

user_hand.add_card(deck.pop_card())
print(user_hand)

user_hand.add_card(deck.pop_card())
print(user_hand)

user_hand.add_card(deck.pop_card())
print(user_hand)

user_hand.add_card(deck.pop_card())
print(user_hand)

user_hand.add_card(deck.pop_card())
print(user_hand)
