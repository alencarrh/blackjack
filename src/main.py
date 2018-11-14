# -*- coding: utf-8 -*-

from src.classes import Deck, Hand

deck = Deck(1)
deck.shuffle()

user_hand = Hand()
dealer_hand = Hand(True)

bet = input('Your bet: ')

end_game = False
round = 0


def give_user_option_to_cut(deck: Deck):
    deck_size = deck.cards_left()
    max_cut = int(deck.cards_left() / 2)

    message = ''.join(["Deck size: ", str(deck_size), "\n", "Max cut: ", str(max_cut), "\n", "Cut at: "])

    position = int(input(message))

    return position


def distribute_initial_cards(_user_hand: Hand, _dealer_hand: Hand, _deck: Deck):
    _user_hand.add_card(_deck.pop_card())
    _dealer_hand.add_card(_deck.pop_card())
    _user_hand.add_card(_deck.pop_card())
    _dealer_hand.add_card(_deck.pop_card())


def show_in_game_info(user_hand: Hand, dealer_hand: Hand):
    print("========================")
    print("Your cards:", ', '.join([str(card) for card in user_hand.cards]))
    print("Your score:", str(user_hand.score))
    print("The dealer shows:", str(dealer_hand.cards[0]))


def check_for_blackjack(user_hand: Hand) -> bool:
    pass


def show_final_result(_user_hand: Hand, _dealer_hand: Hand):
    print("========================")
    print("Your hand:", ', '.join(str(card) for card in _user_hand.cards))
    print("Your score:", str(_user_hand.score))
    print("Dealer's hand:", ', '.join(str(card) for card in _dealer_hand.cards))
    print("Dealer's score:", str(_dealer_hand.score))
    print("========WHO WON HERE=========")
    exit(0)


def show_user_options(round: int):
    first_round = ["or double"]
    option_round = ["Hit", "stay"]
    options = {
        1: option_round + first_round
    }
    print("========================")
    print(', '.join(options.get(round, option_round)), "?")


def execute_action(_user_hand: Hand, _dealer_hand: Hand, _user_action: str, _deck: Deck):
    action = _user_action.lower()
    if action == "hit":
        _user_hand.add_card(_deck.pop_card())
        return

    if action == "double":
        _user_hand.add_card(_deck.pop_card())
        global bet
        bet *= 2

    if action == "stay" or action == "double":
        while _dealer_hand.score < 17:
            _dealer_hand.add_card(_deck.pop_card())

        show_final_result(_user_hand, _dealer_hand)


def check_game_status(_user_hand: Hand, _dealer_hand: Hand):
    if _user_hand.score >= 21:
        show_final_result(_user_hand, _dealer_hand)


give_user_option_to_cut(deck)
distribute_initial_cards(user_hand, dealer_hand, deck)

# TODO refactor this logic
while True:
    round += 1
    show_in_game_info(user_hand, dealer_hand)
    check_game_status(user_hand, dealer_hand)
    show_user_options(round)
    user_action = input("")
    execute_action(user_hand, dealer_hand, user_action, deck)
