from random import randint, choice
import random
from calc import *


def generate_quiz():



    x = randint(0,10)

    y = randint(1,10)
    e = randint(-1,1)
    
    op = choice(['+','-','*','/'])

    r = eval(x, y, op) + e
    return [x,y,op,r,e]
quiz = generate_quiz()
x, y, op, r, e = quiz

output = '{0} {3} {1}= {2}'.format(x,y,r,op)
print(output)
user_answer = input('Y/N? ').upper() 
if e == 0:
    if user_answer == 'Y':
        print('True')
    elif user_answer == 'N':
        print('False')
    else:
        print('Error')
else:
    if user_answer == 'Y':
        print('False')
    elif user_answer == 'N':
        print('True')
    else:
        print('Error')

