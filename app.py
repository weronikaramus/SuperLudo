from flask import Flask, render_template, url_for, jsonify, session, request
from datetime import datetime
from pawn import red_pawns, Pawn
from dice import Dice
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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
    if request.method == 'POST':
        if request.form['submit'] == 'rollDice':
            roll_result = rollDice()
        if request.form['submit'].startswith('move_'):
            index = int(request.form['submit'].split('_')[1])-1
            if 'dice_result' in session:
                result = red_pawns[index].move(session['dice_result'])
                session.pop('dice_result')

    return render_template('game.html', red_pawns=red_pawns, roll_result=roll_result, result=result)

# @app.route('/roll_dice', methods=['POST'])
# def roll_dice():
#     rollDice()

#     return jsonify({'result': dice_result})

if __name__ == "__main__":
    app.run(debug=True)