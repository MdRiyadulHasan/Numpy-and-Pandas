import numpy as np
number = np.random.randint(100, size=(4,6))
max_indeices =np.argmax(number, axis=0)
print(number)
print(max_indeices)
print('\n')
max_indeices=np.argmax(number, axis=1)
print(max_indeices)
max_indeices=np.argmax(number, axis=-1)
print(max_indeices)

















