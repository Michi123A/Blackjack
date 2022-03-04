from turtle import Turtle
import random

SUITS = ["\u2666", "\u2665", "\u2663", "\u2660"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
FONT = "Georgia"


class Card(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.card_values = dict()
        self.cards = list()

    def create_card_deck(self):
        """Creates a deck of cards with suit and rank, and creates a deck of"""
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(suit + "\n" + rank)
                if rank == "J" or rank == "K" or rank == "Q":
                    self.card_values[suit + "\n" + rank] = 10
                elif rank == "A":
                    self.card_values[suit + "\n" + rank] = 11
                else:
                    self.card_values[suit + "\n" + rank] = int(rank)


class Deck(Card):

    def __init__(self):
        super().__init__()
        self.deck = list()
        self.create_card_deck()
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.deck)

    def draw_card(self):
        """Pulls a random card from deck"""
        card = self.deck.pop()
        return card


class Hand(Deck):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = list()
        self.hand = list()

    def add_to_hand(self):
        """Takes drawn card and adds to hand, also takes value and adds to score list"""
        card = self.draw_card()
        self.hand.append(card)
        value = self.card_values[card]
        self.score.append(value)
        return card

    def create_card(self):
        """Creates the card image"""
        if len(self.hand) == 1:
            card = self.hand[0]
        elif len(self.hand) == 2:
            card = self.hand[1]
        else:
            card = self.hand[2]
        self.color("white")
        self.pendown()
        self.begin_fill()
        for i in range(2):
            self.left(90)
            self.forward(110)
            self.left(90)
            self.forward(75)
        self.end_fill()
        self.color("black")
        for i in range(2):
            self.left(90)
            self.forward(110)
            self.left(90)
            self.forward(75)
        self.penup()
        self.backward(37)
        self.left(90)
        self.forward(30)
        self.pendown()
        self.write((card), align="center", font=(FONT, 20, "bold"))
        self.penup()
        self.right(90)

    def cards_image(self, x, y):
        """Takes in coordinates and places the cards image on the board"""
        self.goto(x, y)
        self.create_card()

    def calculate_score(self):
        """Takes the score list and calculates the total"""
        total = 0
        total += sum(self.score)
        if total > 21 and 11 in self.score:
            self.score.remove(11)
            self.score.append(1)
            total = sum(self.score)
        return total

    def find_winner(self, dealer_score):
        """Compares the dealer score and player score each other and 21 to find winner"""
        if self.calculate_score() == dealer_score:
            return "It's a draw."
        elif self.calculate_score() == 21:
            return "Blackjack! You win!"
        elif self.calculate_score() > dealer_score:
            return "You win!"
        elif self.calculate_score() > 21:
            return "Went over 21. You lose."
        elif dealer_score > 21:
            return "You win!"
        elif self.calculate_score() < dealer_score:
            return "Dealer wins."
        elif dealer_score == 21:
            return "Dealer has Blackjack!"

    def clear_cards(self):
        """Clears cards for new game"""
        self.clear()


