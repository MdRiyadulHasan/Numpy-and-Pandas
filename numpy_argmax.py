import numpy as np
data=np.arange(12).reshape(3,4)
print(data)
max_indices=np.argmax(data)
print(max_indices)
#print(data[max_indices])
max_indices_col=np.argmax(data, axis=0)
print(max_indices_col)
max_indices_row=np.argmax(data, axis=1)
print(max_indices_row)