# main.py
import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)

    # Print the result with the expected message
    if isinstance(result, float):
        print(f"The result of the division is {result}") 
    else:
        print(result)  # Print error message if it's not a float

if __name__ == "__main__":
    main()
