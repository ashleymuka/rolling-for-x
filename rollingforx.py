'''
Description:implement a function to roll a die

'''

import random

class GVDie:
    def __init__(self):
        self.my_value = random.randint(1, 6)
        self.rand = random.Random()

    def roll(self):
        self.my_value = self.rand.randint(1, 6)

    def set_seed(self, seed):
        self.rand.seed(seed)

    def compare_to(self, other):
        return self.my_value - other.my_value

def roll_specific_number(die, num, goal):
    rolls = 0
    count = 0

    while count < goal:
        die.roll()
        rolls += 1
        if die.my_value == num:
            count += 1

    return rolls

if __name__ == "__main__":
    seed_value = 15
    random.seed(seed_value)

    die = GVDie()
    die.set_seed(seed_value)

    desired_face = int(input())
    goal_amount = int(input())

    rolls_required = roll_specific_number(die, desired_face, goal_amount)
    
    print(f'It took {rolls_required} rolls to get a "{desired_face}" {goal_amount} times.')




   
