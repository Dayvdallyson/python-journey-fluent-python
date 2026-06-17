import numpy as np

a = np.arange(12)
print(type(a))

print(a.shape)

a.shape = 3, 4

print(a)

print(a[2])

print(a[:, 1])

print(a.transpose())
