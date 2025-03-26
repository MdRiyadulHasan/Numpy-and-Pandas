import numpy as np
arr = np.array([3, 1, 4, 1, 5, 9])
print(np.sort(arr))  # [1, 1, 3, 4, 5, 9]

# Get indices of sorted array
print(np.argsort(arr))  # [1, 3, 0, 2, 4, 5]
