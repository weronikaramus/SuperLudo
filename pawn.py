from dice import Dice
from flask import Flask, render_template, session

app = Flask(__name__)
len = 52
class Pawn:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        # self.superpower = superpower

    def move(self, steps):
        steps = session.get('dice_result', 0)
        self.position = (self.position+steps)%len



red_pawn1 = Pawn("red", 0)
red_pawn2 = Pawn("red", 0)
# red_pawn3 = Pawn("red", 0)
# red_pawn4 = Pawn("red", 0)
red_pawns = [red_pawn1, red_pawn2]
blue_pawn1 = Pawn("blue", len/2)
blue_pawn2 = Pawn("blue", len/2)
# blue_pawn3 = Pawn("blue", len/2)
# blue_pawn4 = Pawn("blue", len/2)