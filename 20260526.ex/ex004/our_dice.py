import random

class Dice:
    def __init__(self):
        self.numbers = []

    def playDice(self):
        self.numbers.append(random.randint(1,6))

    def getNumbers(self):
        return self.numbers
    
    def getSum(self):
        return sum(self.numbers)