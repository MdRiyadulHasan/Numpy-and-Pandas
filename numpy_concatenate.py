import numpy as np
A=np.random.randint(100, size=(4,2))
B=np.random.randint(200, size=(3,2))
#C=np.concatenate((A,B), axis=1) #axis=1 means concatenate in rows
D=np.concatenate((A,B),axis=0) #axis=0 means concatenate in columns
E = np.concatenate((A,B), axis=None)
print(A)
print(B)
print(D)
print(E)