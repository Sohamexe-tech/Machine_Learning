# numpy_basics.py
import numpy as np

def main():
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])

    print("1D Array:")
    print(arr1)

    print("\n2D Array:")
    print(arr2)

    print("\nArray Properties:")
    print("Dimensions:", arr2.ndim)
    print("Shape:", arr2.shape)
    print("Size:", arr2.size)
    print("Data Type:", arr2.dtype)

if __name__ == "__main__":
    main()
