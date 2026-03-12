import numpy as np

a = np.arange(12)
print(a)

b = a.reshape(3, 4)
print(b)

c = a.reshape(2, 2, 3)
print(c)

d = b.flatten()
print(a)

e = a.reshape(-1,1) 
print(e)