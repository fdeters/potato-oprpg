import random


class Die():
    def __init__(self, num_sides: int = 6):
        self.sides = num_sides if num_sides >= 1 else 1  # minimum val of 1
    
    def roll(self):
        return random.randint(1, self.sides)
    