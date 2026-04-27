# create game
# loop:
#   user guesses
#   game responds
# until correct


import random



class Game:
    def __init__(self):
        self.secrate = random.randint( 1 , 100 ) 
    def guess (self, number):
        if number > self.secrate:
            return "too high"
        if number < self.secrate:
            return "too low"
        if number == self.secrate:
            return "correct!"




