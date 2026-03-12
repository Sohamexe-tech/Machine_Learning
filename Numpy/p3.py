import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[arr>25])

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m[1,2])
print(m[:,1])
print(m[0:2, 0:2])

