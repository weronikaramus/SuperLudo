from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
len = 52 # no fields on a board usually 52

class Pawn:
    def __init__(self, color, superpower):
        position = 0
        start = 0
        self.color = color
        self.position = position
        self.start = start

        if self.color == "red":
            self.start = 0
        if self.color == "green":
            self.start = int(len/4)
        if self.color == "blue":
            self.start = int(len/2)
        if self.color == "yellow":
            self.start = int(len/2+len/4)

        self.position = self.start
        self.superpower = superpower
        self.finish = (self.start-2)%len
        self.steps_left = len-2
        self.finished = False

    def kill(self, other_pawn):
        other_pawn.position = other_pawn.start
        other_pawn.steps_left = len-2

    def win(self):
        return redirect(url_for('win'))

    def canMove(self, steps):
        if self.finished == False:
            return self.steps_left-steps >= 0
        else:
            return 0

    def move(self, steps):
        current_position = self.position
        steps = session.get('dice_result', 0)
        new_position = (current_position + steps) % len

        if not self.canMove(steps):
            return 0

        self.steps_left -= steps

        if new_position == self.finish:
            self.position = new_position
            self.finished = True

            if self.color == "red":
                session['red_finished'] += 1
            if self.color == "green":
                session['green_finished'] += 1
            if self.color == "blue":
                session['blue_finished'] += 1
            if self.color == "yellow":
                session['yellow_finished'] += 1

        else:
            self.position = new_position

            for row in pawns:
                for other_pawn in row:
                    if other_pawn.position == new_position and other_pawn != self and other_pawn.color != self.color and not other_pawn.finished:
                        if other_pawn.superpower == "immortal":
                            break
                        elif other_pawn.superpower == "reversedkill":
                            if other_pawn.position is not other_pawn.start:
                                self.position = self.start
                                self.steps_left = len-2
                        else: self.kill(other_pawn)

pawns = [[Pawn("Empty", "Empty") for _ in range(4)] for _ in range(4)]
pawns[0][0] = Pawn("red", "normal")
pawns[0][1] = Pawn("red", "freeleave")
pawns[0][2] = Pawn("red", "immortal")
pawns[0][3] = Pawn("red", "reversedkill")
pawns[1][0] = Pawn("green", "normal")
pawns[1][1] = Pawn("green", "freeleave")
pawns[1][2] = Pawn("green", "immortal")
pawns[1][3] = Pawn("green", "reversedkill")
pawns[2][0] = Pawn("blue", "normal")
pawns[2][1] = Pawn("blue", "freeleave")
pawns[2][2] = Pawn("blue", "immortal")
pawns[2][3] = Pawn("blue", "reversedkill")
pawns[3][0] = Pawn("yellow", "normal")
pawns[3][1] = Pawn("yellow", "freeleave")
pawns[3][2] = Pawn("yellow", "immortal")
pawns[3][3] = Pawn("yellow", "reversedkill")

