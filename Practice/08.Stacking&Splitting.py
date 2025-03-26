import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vertical stack
print(np.vstack((a, b))) 

# Horizontal stack
print(np.hstack((a, b)))

# Split array
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.split(arr, 3))  # [array([1,2]), array([3,4]), array([5,6])]
