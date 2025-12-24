# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# input csv file
dataFrame = pd.read_csv("C:\\Users\\ayush\\Mall_Customers.csv")

print("Our DataFrame...",dataFrame)