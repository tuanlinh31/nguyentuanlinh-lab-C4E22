from random import *
from calc import *
import random
from add_game import *


def check_answer(x, y, op, r, user_choice):
    if user_choice == True:
        if r == eval(x,y,op):
            return True
        else:
            return False
    else:
        if r == eval(x,y,op):
            return False
        else:
            return True
