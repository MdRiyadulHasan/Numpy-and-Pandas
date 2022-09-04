import numpy as np
data=np.array([
    [30,21,45],
    [50,12,10],
    [25,70,62]
])
print(data)
# flatten into 1D array
print(np.sort(data, axis=None))
# sorting according to row
print(np.sort(data, axis=-1))
# sorting according to columns
print(np.sort(data, axis=0))