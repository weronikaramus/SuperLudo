import random
from flask import session

def rollDice():
    dice_result = random.randint(1, 6)
    session['dice_result'] = dice_result
    return dice_result