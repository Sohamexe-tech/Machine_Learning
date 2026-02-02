# array_creation.py
import numpy as np

def main():
    zeros_array = np.zeros((2, 3))
    ones_array = np.ones((3, 2))
    range_array = np.arange(1, 11, 2)
    linspace_array = np.linspace(1, 10, 5)

    print("Zeros Array:\n", zeros_array)
    print("\nOnes Array:\n", ones_array)
    print("\nRange Array:\n", range_array)
    print("\nLinspace Array:\n", linspace_array)

if __name__ == "__main__":
    main()
