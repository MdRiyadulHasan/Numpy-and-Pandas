import numpy as np
# numbers between 5 and 50, total 24
numbers = np.linspace(5,50,24, dtype=int)
print(numbers)
numbers=numbers.reshape(4,-1)
# number which is divided by 4 is stored in mask
mask=numbers%4==0
print(numbers[mask])
divide_by_3 = numbers[numbers%3==0]
print(divide_by_3)
