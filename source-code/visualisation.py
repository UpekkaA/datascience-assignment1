# MS - INIT file; importing CSV data and printing it 

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

# Print a pie chart of 
labels = ['Black', 'Red', 'Brown']

# frequency count
hair_colour_freq = [5, 3, 2]  # Black, Red, Brown

# colours
colours = ['yellowgreen', 'gold', 'lightskyblue']

fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(hair_colour_freq, colors=colours, labels=labels, shadow=True, 
       explode=(0, 0.1, 0), startangle=90, autopct="%1.1f")