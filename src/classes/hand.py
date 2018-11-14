# -*- coding: utf-8 -*-

from .card import Card
from .number import Number


class Hand:

    def __init__(self, dealer=False):
        self.__cards = []
        self.__print_suit = True
        self.__dealer = dealer

    @property
    def score(self) -> int:
        """
        Calculate the score of the hand
        :return:
        """
        # TODO review this logic
        # maybe pass the cards to another method and  this method calculates the score

        number_of_aces = self.cards.count(Number.ACE)
        score = sum(self.cards)

        score += (10 * number_of_aces)

        if score > 21:
            for i in range(number_of_aces):
                score -= 10
                if score < 22:
                    break

        return score

    @property
    def cards(self):
        """
        Returns the card in the hand
        :return:
        """
        return self.__cards

    @property
    def is_dealer(self):
        return self.__dealer

    def add_card(self, card: Card):
        """
        Add a card to the hands
        :param card:
        :return:
        """
        self.__cards.append(card)

    def __str__(self):
        # TODO the print of the cards (of dealer) will depend in the round/context of the game, so problably it can't
        # be done in the __str__ method but by some other plase/method/function/animal/alien/fish
        # Maybe in this place, I can considerer the more detailed print that is going to be show in the end of the game
        if self.__dealer:
            return ''.join(["Dealer's hand: ", str(self.cards), "\n", "Dealer's score: ", str(self.score)])
        return ''.join(["Your hand: ", str(self.cards), "\n", "Your score: ", str(self.score)])
