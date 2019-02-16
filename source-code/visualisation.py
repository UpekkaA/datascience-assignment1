# MS - INIT file; importing CSV data and printing it 
# MS - Accessed matrix column of "married" 

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

# Extract the unique marital-statuses

# Extract the marital status column from matrix
marital_statuses = df.loc[: , "married"]

statuses = []

# Loop through the statuses and count the number of instances for each marital status; 
# store that in an array in the same order as what is in "statues"
counts = [1, 2, 3] # hard-coded for now

# Print the labels 
labels = statuses

# Specify the colours 
colours = ['yellowgreen', 'gold', 'lightskyblue']

# Produce the plot
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(counts, colors=colours, labels=labels, shadow=True, 
       explode=(0, 0.1, 0), startangle=90, autopct="%1.1f")