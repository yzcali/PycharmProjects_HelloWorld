# look at page https://docs.python.org/3/py-modindex.html
import random

for i in range(3):
    print(random.randint(10, 99))  # everytime run it gives you different 3 numbers
print()

# to select a leader team we make a programme
members = ['john', 'mary', 'alex', 'marty', 'gloria', 'melvin']
leader = random.choice(members)
print(leader)  # mary but next time it can be changed
print()


# make a programme for select two dices like (3,1)
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())  # same (1,4)
