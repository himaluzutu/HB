from random import randint

class Dice:
    """Class for simulating the outcome of the dice throw experiment"""
    def __init__(self,num_of_dice_sides=6):
        self.num_of_dice_sides=num_of_dice_sides



    def dice_roll(self):
        """Return the outcome of every dice roll in the experiment."""
        return randint(1,self.num_of_dice_sides)


