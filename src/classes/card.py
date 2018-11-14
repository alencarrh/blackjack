# -*- coding: utf-8 -*-
from .number import Number
from .suit import Suit


class Card:

    def __init__(self, number: Number, suit: Suit, value=None, show_suit=False):
        self.__number = number
        self.__suit = suit
        self.__value = value
        self.__show_suit = show_suit

    @property
    def number(self) -> Number:
        return self.__number

    @property
    def suit(self) -> Suit:
        return self.__suit

    @property
    def value(self):
        return self.__value

    def toggle_suit(self):
        """
        Toogle the value of the flag that indicates if it should print the suit of the card or not
        """
        self.__show_suit = not self.__show_suit

    def __radd__(self, other):
        return self.value + other

    def __add__(self, other):
        return self.value + other.value

    def __eq__(self, other) -> bool:
        if isinstance(other, Number):
            return self.number == other
        return self.number == other.number and self.suit == other.suit

    def __str__(self) -> str:
        if self.__show_suit and self.suit:
            return ' '.join([self.number.name, "of", self.suit.name])
        return self.number.name

    def __repr__(self) -> str:
        return self.__str__()
