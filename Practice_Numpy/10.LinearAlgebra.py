import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
print(np.dot(A, B))

# Determinant
print(np.linalg.det(A))

# Inverse
print(np.linalg.inv(A))

# Eigenvalues & Eigenvectors
vals, vecs = np.linalg.eig(A)
print(vals, vecs)
