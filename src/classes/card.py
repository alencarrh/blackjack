# -*- coding: utf-8 -*-
from .number import Number
from .suit import Suit


class Card:

    def __init__(self, number: Number, suit: Suit, value=None):
        self.__number = number
        self.__suit = suit
        self.__value = value

    @property
    def number(self) -> Number:
        return self.__number

    @property
    def suit(self) -> Suit:
        return self.__suit

    @property
    def value(self):
        return self.__value

    def __eq__(self, other) -> bool:
        return self.number == other.number and self.suit == other.suit

    def __str__(self) -> str:
        return ' '.join([self.number.name, "of", self.suit.name])

    def __repr__(self) -> str:
        return self.__str__()
