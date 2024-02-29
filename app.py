from flask import Flask, render_template, session, request, redirect, url_for
from pawn import pawns
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

colors = ["red", "green", "blue", "yellow"]

# Define the dictionary manually
board_dictionary = {91: 0, 92: 1, 93: 2, 94: 3, 95: 4, 81: 5, 66: 6, 51: 7, 36: 8, 21: 9, 6: 10, 7: 11, 8: 12, 23: 13, 38: 14, 53: 15, 68: 16, 83: 17, 99: 18, 100: 19, 101: 20, 102: 21, 103: 22, 104: 23, 119: 24, 134: 25, 133: 26, 132: 27, 131: 28, 130: 29, 129: 30, 143: 31, 158: 32, 173: 33, 188: 34, 203: 35, 218: 36, 217: 37, 216: 38, 201: 39, 186: 40, 171: 41, 156: 42, 141: 43, 125: 44, 124: 45, 123: 46, 122: 47, 121: 48, 120: 49, 105: 50, 90: 51}


def rollDice():
    dice_result = random.randint(1, 6)
    session['dice_result'] = dice_result
    return dice_result

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    session['red_finished'] = 3
    session['green_finished'] = 3
    session['blue_finished'] = 3
    session['yellow_finished'] = 3

    roll_result = None
    result = None
    index = None
    color = None
    current_player = session.get('current_player', 0)

    if request.method == 'POST':
        if request.form['submit'] == 'rollDice':
            roll_result = rollDice()

        if not (any(pawn.canMove(session.get('dice_result', 0)) for pawn in pawns[current_player])):
            current_player = (current_player + 1) % len(colors)
            session['current_player'] = current_player

        if request.form['submit'].startswith('move_'):
            if 'dice_result' in session:
                index = int(request.form['submit'].split('_')[2])
                color = colors.index(request.form['submit'].split('_')[1])
                print(index, color)
                result = pawns[color][index].move(session['dice_result'])

                if session['dice_result'] != 6:
                    current_player = (current_player + 1) % len(colors)
                    session['current_player'] = current_player
                    session.pop('dice_result')

    if session['red_finished'] == 4 or session['green_finished'] == 4 or session['blue_finished'] == 4 or session['yellow_finished'] == 4:
        return redirect(url_for('win'))

    return render_template('game.html', pawns=pawns, roll_result=roll_result, result=result, colors=colors, current_player=current_player, color=color, index=index, board_dictionary=board_dictionary)

@app.route('/win', methods=['GET', 'POST'])
def win():
    winner = colors[session['current_player']-1]
    return render_template('win.html', winner=winner)

if __name__ == "__main__":
    app.run(debug=True)