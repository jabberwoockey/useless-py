#!/usr/bin/env python3
# In order to run the script plotly package should be installed:
# pip3 install plotly

from random import randint
from sys import argv, exit
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create a die class
class Die:
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
    def __str__(self):
        return f'A {self.num_sides}-sided die.'
    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

# Initial variables
times = 1000

# Create dice
if len(argv) == 1:
    script = argv
    print(f'Usage: {script[0]} [<die> [<die>] ...] [number of times]\n' +
        f' '*7+f'{script[0]} 6 (for d6 1000 times)\n' +
        f' '*7+f'{script[0]} 6 1000 (for d6 and d10 10000 times)\n' +
        f' '*7+f'{script[0]} 6 10 10000 (for d6 and d10 10000 times)\n' +
        f' '*7+f'{script[0]} 100 100 100 100000 (for three d100 100000 times)')
    exit(1)
elif len(argv) == 2:
    script, sides = argv
    dice = [Die(int(sides))]
else:
# len(argv) > 2:
    script, *sides_list, times = argv
    dice = [Die(int(sides)) for sides in sides_list]

dice_sting = ["d" + str(die.num_sides) for die in dice]

# Make some rolls, and store results in a list
results = [sum([die.roll() for die in dice]) for i in range(int(times))]

# Analyze the results
max_result = sum([die.num_sides for die in dice])
min_result = len(dice)
frequencies = [results.count(i) for i in range(min_result, max_result+1)]

# Create a .csv and print results on the screen
filename = f'{"_".join(dice_sting)}_{times}times'
with open(f'{filename}.csv', 'w') as f:
    f.write('number,frequency\n')
    for i in range(min_result, max_result+1):
        print(f'{i:>3}: {frequencies[i - min_result]:>7}')
        f.write(f'{i},{frequencies[i - min_result]}\n')
print('-' * 12 + '\n' + f'   {sum(frequencies):>9}')

# Visualize the results
x_values = list(range(min_result, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling the dice ' +
                         f'{", ".join(dice_sting)} ' +
                         f'{times} times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout},
             filename=f'{filename}.html')
