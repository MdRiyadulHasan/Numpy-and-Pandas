import numpy as np
A = np.arange(30).reshape(3,1,10)
print(A)
B = np.arange(50).reshape(1,5,10)
print(B)
# Broadcasting image
C=A+B
print(f'Broadcasting Numpy array : \n  {C}')