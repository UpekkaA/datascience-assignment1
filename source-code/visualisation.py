# MS - INIT file; importing CSV data and printing it 
# MS - Accessed matrix column of "married" 
# MS - Seperated out two arrays one containing individual marital statuses and the other with counts for each status

import numpy as np
import csv

# Import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline

# Import panda
import pandas as pd

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

# Print the labels 
labels = statuses

# Specify the colours 
colours = ['yellowgreen', 'gold', 'lightskyblue', 'red', 'green', 'purple', 'orange']

# Produce the plot
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(counts, colors=colours, labels=labels, shadow=True, 
       explode=(0, 0.1, 0, 0, 0, 0, 0), startangle=90, autopct="%1.1f")