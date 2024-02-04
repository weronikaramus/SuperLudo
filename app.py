from flask import Flask, render_template, url_for, jsonify, session, request
from datetime import datetime
from pawn import pawns
from dice import Dice
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

colors = ["red", "blue", "yellow", "green"]

def rollDice():
    dice_result = random.randint(1, 6)
    session['dice_result'] = dice_result
    return dice_result


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['GET','POST'])
def game():
    roll_result = None
    result = None
    index = None
    color = None
    if request.method == 'POST':
        if request.form['submit'] == 'rollDice':
            roll_result = rollDice()
        if request.form['submit'].startswith('move_'):
            if 'dice_result' in session:
                index = int(request.form['submit'].split('_')[2])
                color = colors.index(request.form['submit'].split('_')[1])
                print(index, color)
                result = pawns[color][index].move(session['dice_result'])
                session.pop('dice_result')

    return render_template('game.html', pawns=pawns, roll_result=roll_result, result=result)


if __name__ == "__main__":
    app.run(debug=True)