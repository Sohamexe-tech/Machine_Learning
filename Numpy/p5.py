# indexing_slicing.py
import numpy as np

def main():
    arr = np.array([10, 20, 30, 40, 50])
    matrix = np.array([[1, 2, 3], [4, 5, 6]])

    print("Array:", arr)
    print("First element:", arr[0])
    print("Last element:", arr[-1])
    print("Slice (1 to 3):", arr[1:4])

    print("\nMatrix:\n", matrix)
    print("Element at (0,1):", matrix[0, 1])
    print("Second column:", matrix[:, 1])

if __name__ == "__main__":
    main()
