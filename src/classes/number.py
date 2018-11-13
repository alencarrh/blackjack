# -*- coding: utf-8 -*-
from enum import Enum


def build_number(_id, name):
    """
    TODO I don't really know if this method should be here. I'll check the best way at some point in the future
    """
    return {
        "id": _id,
        "name": name
    }


class Number(Enum):
    ACE = build_number(1, "Ace")
    TWO = build_number(2, "2")
    THREE = build_number(3, "3")
    FOUR = build_number(4, "4")
    FIVE = build_number(5, "5")
    SIX = build_number(6, "6")
    SEVEN = build_number(7, "7")
    EIGHT = build_number(8, "8")
    NINE = build_number(9, "9")
    TEN = build_number(10, "10")
    JACK = build_number(11, "Jack")
    QUEEN = build_number(12, "Queen")
    KING = build_number(13, "King")

    @property
    def id(self):
        return self._value_["id"]

    @property
    def name(self):
        return self._value_["name"]

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name
