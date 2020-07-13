""" Cracking the Coding Interview, 6th Edition - Python Solutions
7.1 Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
subclass the data structures to implement blackjack.
"""
import unittest
from unittest import TestCase
import random


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def draw_card(self):
        return self.cards.pop()

    def shuffle_deck(self):
        for index in range(len(self.cards)):
            swap_index = random.randint(0, index)
            self.cards[index], self.cards[swap_index] = self.cards[swap_index], self.cards[index]


class Hand:
    def __init__(self, cards=None):
        if not cards:
            self.cards = []
        else:
            self.cards = cards
        self.hand_value = 0

    def get_hand_value(self):
        return self.hand_value

    def add_card(self, card):
        self.hand_value += card.value
        self.cards.append(card)


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class BlackjackHand(Hand):
    def get_blackjack_value(self):
        num_aces = 0
        full_value = self.get_hand_value()

        for card in self.cards:
            if card.value == 1:
                num_aces += 1
        while full_value <= 10:
            if num_aces > 0:
                full_value += 11
                num_aces -= 1
        return full_value

    def is_blackjack(self):
        return True if self.get_blackjack_value() == 21 else False


class TestDeckOfCards(TestCase):
    def testA(self):
        cards = []
        suits = ['spade', 'diamond', 'club', 'heart']
        for suit in suits:
            for value in range(1, 14):
                cards.append(Card(value, suit))
        deck = Deck(cards)

        for card in deck.cards:
            print(card.value, card.suit)

        self.assertEqual(deck.draw_card().value, 13)
        self.assertEqual(deck.draw_card().suit, 'heart')

        deck.shuffle_deck()
        print('After shuffle...')
        for card in deck.cards:
            print(card.value, card.suit)

    def testB(self):
        cards = []
        suits = ['spade', 'diamond', 'club', 'heart']
        for suit in suits:
            for value in range(1, 14):
                cards.append(Card(value, suit))
        deck = Deck(cards)
        deck.shuffle_deck()

        hand = BlackjackHand()
        for _ in range(2):
            hand.add_card(deck.draw_card())
        print("Hand value: {} and blackjack value: {}".format(hand.get_hand_value(), hand.get_blackjack_value()))


if __name__ == "__main__":
    unittest.main()
