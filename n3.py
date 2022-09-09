# Write a python program to find the maximum and minimum value in a given 2-D array
import numpy as np 

my2darray = [[746,93],[100, 899]]

# this prints the maximum value in the 2D array - using the python inbuilt max method
print(max(max(my2darray, key = max)))

# this prints the minimum value in the 2D array - using the python inbuilt min method
print(min(min(my2darray, key = min)))
