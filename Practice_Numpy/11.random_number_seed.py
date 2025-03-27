import numpy as np
np.random.seed(42)  # Ensures reproducibility
print(np.random.rand(3, 3))  # Random numbers (0 to 1)

print(np.random.randint(1, 10, (2, 2)))  # Random integers
print(np.random.normal(0, 1, (3, 3)))  # Normal distribution
