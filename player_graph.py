# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

name = str(input("Player name: "))
position = str(input("Player Position: "))

atributes = ["Attacking", "Technique", "Tactic", "Defense", "Creativity"]
values = []

for atributo in atributes:
    value = int(input(atributo + ": "))
    values.append(value)

overall = int(sum(values)/len(values))

# Set data
df = pd.DataFrame({
'group': ['A'],
f'ATT {[values[0]]}': [values[0]],
f'TEC {[values[1]]}': [values[1]],
f'TAC {[values[2]]}': [values[2]], 
f'DEF {[values[3]]}': [values[3]],
f'CRE {[values[4]]}': [values[4]]
})
 
# ------- PART 1: Create background
 
# number of variable
categories=list(df)[1:]
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30,40,50,60,70,80,90,100], ["10","20","30","40","50","60","70","80","90","100"], color="grey", size=7)
plt.ylim(0,100)
 

# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't make a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label=name)
ax.fill(angles, values, 'b', alpha=0.1)
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Show the overall rating
plt.text(-100, 120, f"Overall Rating: {overall}", ha="left", va="top")

# Show the graph
plt.show()