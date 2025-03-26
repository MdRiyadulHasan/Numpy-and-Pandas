import numpy as np

data = np.random.randint(50, 100, (5, 5))  # Random 5x5 matrix
print("Data:\n", data)

print("Mean:", np.mean(data, axis=0))  # Column-wise mean
print("Sum:", np.sum(data, axis=1))    # Row-wise sum
