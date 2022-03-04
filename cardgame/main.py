from turtle import Screen
from card import Hand
from board import Board, WhoWins

s = Screen()
board = Board()
s.listen()
s.bgcolor("red")

board.create_board()
announce = WhoWins()
dealer = Hand("Dealer")
player = Hand("Player")

def start_game():
    """Starts the game with dealer card and player's two cards"""
    dealer.add_to_hand()
    dealer.cards_image(-90, -10)
    dealer.add_to_hand()
    player.add_to_hand()
    player.cards_image(-90,-190)
    player.add_to_hand()
    player.cards_image(160, -190)


def stay():
    """Reveals all cards and winner"""
    dealer.cards_image(160, -10)
    dealer_score = dealer.calculate_score()
    player_score = player.calculate_score()
    winner = player.find_winner(dealer_score)
    announce.announce_winner(winner)

def draw():
    """Draws another card for player and reveals all cards and winner"""
    player.add_to_hand()
    player.cards_image(37, -190)
    stay()

def new_game():
    """Clears the cards and winner announcement for new game"""
    announce.clear_winner()
    dealer.clear_cards()
    player.clear_cards()
    player.hand.clear()
    dealer.hand.clear()


s.onkey(key="p", fun=start_game)
s.onkey(key="space", fun=new_game)
s.onkey(key="d", fun=draw)
s.onkey(key="s", fun=stay)

s.exitonclick()