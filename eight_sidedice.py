#    15-6. Two D8s: Create a simulation showing what happens when you roll two
#    eight-sided dice 1,000 times. Try to picture what you think the visualization will
#    look like before you run the simulation, then see if your intuition was correct.
#    Gradually increase the number of rolls until you start to see the limits of your
#    system’s capabilities.

import plotly.express as hb

from dice import Dice

results=[]

first_die_sides=int(input("Enter the number of sides for the first dice: "))
second_die_sides=int(input("Enter the number of sides for the second dice: "))

die_1=Dice(first_die_sides)
die_2=Dice(second_die_sides)

dice_roll_1=die_1.num_of_dice_sides
dice_roll_2=die_2.num_of_dice_sides

num_of_simulations=int(input("Enter the number of dice throws: "))

for num_rolls in range(num_of_simulations):
    result=die_1.dice_roll()+die_2.dice_roll()
    results.append(result)

max_outcome=(die_1.num_of_dice_sides+die_2.num_of_dice_sides)

possible_outcomes=range(2,max_outcome)

num_of_outcome_value_appears=[]
for num_of_outcome in possible_outcomes:
    count_of_number=results.count(num_of_outcome)
    num_of_outcome_value_appears.append(count_of_number)

print(num_of_outcome_value_appears)

title=f"Number of Rolls for two separate Dices with the first dice having {die_1.num_of_dice_sides} sides & the second dice having {die_2.num_of_dice_sides} sides."
labels={"x":"Combined Roll Outcome Number","y":"Frequency of Number"}

fig=hb.bar(x=possible_outcomes,y=num_of_outcome_value_appears,title=title,labels=labels)
fig.update_layout(xaxis_dtick=1)

path_folder=f"C:/Users/USER/Desktop/Python Books/first_die sides_{die_1.num_of_dice_sides} & second_die sides_{die_2.num_of_dice_sides} .html"
fig.write_html(path_folder)
#fig.show()

