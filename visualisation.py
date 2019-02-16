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