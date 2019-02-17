# MS - INIT file; importing CSV data and printing it 
# MS - Accessed matrix column of "married" 
# MS - Seperated out two arrays one containing individual marital statuses and the other with counts for each status
# MS - Set properties of pie chart plot; imported and used mpld3 to render it as HTML and open it in browser

import numpy as np
import csv

# Import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline

# Import panda
import pandas as pd

# Import mpld3 to produce visualisation output as HTML
import mpld3

# Convert the CSV data into a matrix
df = pd.read_csv("resources/PSID.csv")
df.as_matrix()

# Print the contents
print (df)


# Print a pie chart based on marital status

# Extract the marital status column from matrix
marital_statuses = df.loc[: , "married"]

# Extract the unique marital-statuses
stats_ordered = {}

for mar_stat in marital_statuses:
	if mar_stat in stats_ordered: 
		stats_ordered[mar_stat] += 1
	else:
		stats_ordered[mar_stat] = 1

print(stats_ordered)

# Create separate arrays; place in each array the each marital-status instance and its respective count
statuses = []
counts = []

for key, value in stats_ordered.items():
	statuses.append(key)
	counts.append(value)

print("Printing statuses:")
print(statuses)
print("Printing counts: ")
print(counts)

# Specify the colours 
colours = ['yellowgreen', 'gold', 'lightskyblue', 'red', 'green', 'purple', 'orange']

# Produce the plot
fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(
	counts, 
	# labels=statuses, 
	# labeldistance=1.1, 
	shadow=True, 
	startangle=90, 
	autopct="%1.1f"
	)

# Set the legend
ax.legend(
	wedges, 
	statuses,
	title="Marital Statuses",
	loc="center right",
	bbox_to_anchor=(0.7, 0., 0.55, 1)
	)

# Set properties of of text that displays wedge values
plt.setp(autotexts, size=12, weight="bold", color="white")

# Set properties of title
titlefont = {'fontname':'Helvetica'}

ax.set_title(
	"Distribution of marital status in the sample", 
	{'fontsize': 10, 'fontweight': 5}, 
	loc="center", 
	**titlefont
	)

# Render the plot as HTML
mpld3.show(fig)