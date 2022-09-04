import numpy as np
A=np.random.randint(50,size=(3,4))
B=np.random.randint(40,size=(3,2))
C=np.hstack((A,B))
print(A)
print(B)
print(C)