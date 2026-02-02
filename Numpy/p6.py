# array_operations.py
import numpy as np

def main():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("Array A:", a)
    print("Array B:", b)

    print("\nAddition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

    print("\nScalar Operations:")
    print("Multiply by 10:", a * 10)
    print("Add 5:", a + 5)

if __name__ == "__main__":
    main()
