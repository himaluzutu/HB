from dice import Dice

import plotly.express as hb

results=[]

die_1=Dice(10)
die_2=Dice(10)
for num_of_die_roll in range(50000):
    result=die_1.dice_roll()+die_2.dice_roll()
    results.append(result)

max_dice_sides=die_1.num_of_dice_sides*2
possible_values=range(2,max_dice_sides+1)

frequencies=[]
for dice_outcome in possible_values:
    frequency=results.count(dice_outcome)
    frequencies.append(frequency)

print(frequencies)

title="Results of Rolling D6 and D10 Dices 50,000 Times"
labels={"x":"Results","y":"Frequencies of Results"}

fig=hb.bar(x=possible_values,y=frequencies,title=title,labels=labels)
fig.update_layout(xaxis_dtick=1)
path_folder="C:/Users/USER/Desktop/Python Books/figure.html"
fig.write_html(path_folder)
fig.show()
