# math_functions.py
import numpy as np

def main():
    arr = np.array([4, 9, 16, 25])

    print("Array:", arr)
    print("Square Root:", np.sqrt(arr))
    print("Maximum:", np.max(arr))
    print("Minimum:", np.min(arr))
    print("Sum:", np.sum(arr))
    print("Mean:", np.mean(arr))

if __name__ == "__main__":
    main()
