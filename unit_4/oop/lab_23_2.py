import random

class Dice:

    def __init__(self):
        self.value = None

    def throw(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        return "[{}]".format(self.value)

class DicePair:
    def __init__(self):
        self.pair = [Dice(), Dice()]

    def throw(self):
        self.pair[0].throw()
        self.pair[1].throw()

    def is_double(self):
        return self.pair[0].value == self.pair[1].value

    def __str__(self):
        return str(self.pair[0]) + str(self.pair[1])

dices = DicePair()

while True:
    dices.throw()
    print(dices)
    if dices.is_double():
        break