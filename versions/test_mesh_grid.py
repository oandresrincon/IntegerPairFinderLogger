import numpy as np
import time

limit=10

a_values = np.arange(2, limit)
b_values = np.arange(2, limit)

a, b = np.meshgrid(a_values, b_values)  # Create a grid of 'a' and 'b' values

print(a, b)
