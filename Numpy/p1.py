import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([[1,2,3],[4,5,6]])
           
print(a.shape) #(5,)
print(b.shape) #(2,3)
print(a.ndim) #1 dimension
print(b.ndim) #2 dimensions
print(a.dtype) #int64
print(b.dtype) #int64

zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
eye = np.eye(3)
rand = np.random.rand(3, 3)
randn = np.random.randn(3, 3)
arange = np.arange(0, 10, 2)
linespace = np.linspace(0, 1, 5)

print(zeros)
print(ones) 
print(eye)  
print(rand) 
print(randn)
print(arange)
print(linespace)
