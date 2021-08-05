#numpy cheatsheet

# importing the numpy module
import numpy as np

# creating a numpy array
data = np.array([1000, 2500, 1400, 1800, 900, 4200, 2200, 1900, 3500])

# creating a new variable to be added to the array
newHouse = int(input("Enter new square footage: "))

# adding a new value to the array
data = np.append(data, newHouse)

# PERFORMING OPERATIONS IN THE ARRAY
print(f"Sorted numpy array: {np.sort(data)}")    # sorting the array
print(f"Standard Deviatioin of the array: {np.std(data)}")     # standard deviation of data
print(f"Variance of the array: {np.var(data)}")     # variance of data
print(f"Mean of the array: {np.mean(data)}")        # mean of data
print(f"Median of the array: {np.median(data)}")    # median of data

