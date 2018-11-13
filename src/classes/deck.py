# -*- coding: utf-8 -*-
import random

from .card import Card
from .number import Number
from .suit import Suit


class Deck:
    deck_max_value = 10

    def __init__(self):
        self.cards = self.__initialize_deck()

    def __initialize_deck(self):
        """
        Create exacly one deck. The deck has all cards, one for each suit.

        :return: All the cards that the deck will have.
        """
        cards = []
        for suit in Suit:
            for number in Number:
                card = Card(number, suit, min(number.id, self.deck_max_value))
                cards.append(card)

        return cards

    def shuffle(self):
        """
        Shuffles the deck
        """
        random.shuffle(self.cards)

    def cut(self, position):
        """
        cut the deck in the position indicated and ignore the position card and all cards above.
        :param position: position to cut
        """
        self.cards = self.cards[position + 1:]

    def get_card(self) -> Card:
        """
        This method will always return the top card in the deck.
        :return: the top card of the deck
        """
        return self.cards.pop(0)

    def reset(self):
        """
        This method will recreate the deck with all the cards.
        It doesn't shuffle the deck.
        """
        self.cards = self.__initialize_deck()
