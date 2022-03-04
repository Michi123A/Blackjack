from turtle import Turtle

ALIGN = "center"
FONT = "Verdana"


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fast")

    def create_board(self):
        """Creates title and label for where dealer/player cards will be placed"""
        self.color("black")
        self.goto(0, 250)
        self.write("Let's play a game of Blackjack", align=ALIGN,font=(FONT, 28, "bold"))
        self.goto(0, 210)
        self.write("Press 'p' to play, 'd' to draw, 's' to stay and 'space' to start over.", align=ALIGN, font=(FONT, 14, "bold"))
        self.goto(0, 130)
        self.color("yellow")
        self.write("Dealer", align=ALIGN, font=(FONT, 24, "underline"))
        self.goto(0, -60)
        self.write("Player", align=ALIGN, font=(FONT, 24, "underline"))


class WhoWins(Board):

    def __init__(self):
        super(WhoWins, self).__init__()
        self.color("purple")

    def announce_winner(self, winner):
        """Reveals the winner"""
        self.goto(0,0)
        self.write(winner, align=ALIGN, font=("Arial", 44, "bold"))

    def clear_winner(self):
        """Clears announcement"""
        self.clear()