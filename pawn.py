from dice import Dice
from flask import Flask, render_template, session

app = Flask(__name__)
len = 52
class Pawn:
    def __init__(self, color):
        position = 0
        start = 0
        self.color = color
        self.position = position
        self.start = start
        if self.color == "red":
            self.start = 0
        if self.color == "blue":
            self.start = len/2


        self.position = self.start
        # self.superpower = superpower

    def kill(self, other_pawn):
        other_pawn.position = other_pawn.start

    def move(self, steps):
        current_position = self.position
        steps = session.get('dice_result', 0)
        new_position = (current_position + steps) % len

        # Check if the new position overlaps with any other pawn's position
        for row in pawns:
            for other_pawn in row:
                if other_pawn.position == new_position and other_pawn != self:
                    # Call the "kill" function when a collision is detected
                    self.kill(other_pawn)

        self.position = new_position

    # def move(self, steps):
    #     steps = session.get('dice_result', 0)
    #     new_position = (self.position+steps)%len
    #     for row in pawns:
    #         for other_pawn in row:
    #             if other_pawn.position == new_position and other_pawn != self and other_pawn.position != other_pawn.start:
    #                 self.kill(other_pawn)
    #     self.position = new_position




pawns = [[Pawn("Empty") for _ in range(2)] for _ in range(2)]
pawns[0][0] = Pawn("red")
pawns[0][1] = Pawn("red")
pawns[1][0] = Pawn("blue")
pawns[1][1] = Pawn("blue")