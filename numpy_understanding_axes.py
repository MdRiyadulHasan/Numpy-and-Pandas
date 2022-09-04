import numpy as np
numbers=np.array([
    [50,32,78,15],
    [82,65,70,92],
    [18,52,35,42],
    [40,95,54,39]
])
# max from numpy.array
print(numbers.max())
# axis =0, columns and axis=1 rows
# max from all columns
print(numbers.max(axis=0))
# max from all rows
print(numbers.max(axis=1))
