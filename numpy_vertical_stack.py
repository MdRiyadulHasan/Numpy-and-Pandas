import numpy as np
A=np.random.randint(100,size=(2,5))
B=np.random.randint(50,size=(3,5))
# vertical_stack
C=np.vstack((A,B))
print(A)
print(B)
print(C)