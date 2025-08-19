from dice import Dice

import plotly.express as hb

results=[]

die_1=Dice()
die_2=Dice()
for num_of_die_roll in range(1001):
    result=die_1.dice_roll()+die_2.dice_roll()
    results.append(result)

max_dice_sides=die_1.num_of_dice_sides*2
possible_values=range(2,max_dice_sides+1)

frequencies=[]
for dice_outcome in possible_values:
    frequency=results.count(dice_outcome)
    frequencies.append(frequency)

print(frequencies)

title="Results of Rolling Two Six Sided Die 1,000 Times"
labels={"x":"Results","y":"Frequencies of Results"}

fig=hb.bar(x=possible_values,y=frequencies,title=title,labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()


