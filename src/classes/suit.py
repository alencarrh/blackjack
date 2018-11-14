# -*- coding: utf-8 -*-
from enum import Enum


def build_suit(_id, name):
    return {
        "id": _id,
        "name": name
    }


class Suit(Enum):
    CLUB = build_suit(1, "Club")
    HEART = build_suit(2, "Heart")
    DIAMOND = build_suit(3, "Diamond")
    SPADE = build_suit(4, "Spade")

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
