def perform_operation(num1, num2, operation):
  """Performs an arithmetic operation based on the provided parameters.
  Args:
    num1: The first number.
    num2: The second number.
    operation: The operation to perform ('add', 'subtract', 'multiply', 'divide').
  Returns:
    The result of the operation, or a specific message for division by zero.

  Raises:
    ValueError: If the operation parameter is invalid.
  """
  if operation == 'add':
    return num1 + num2
  elif operation == 'subtract':
    return num1 - num2
  elif operation == 'multiply':
    return num1 * num2
  elif operation == 'divide':
    if num2 == 0:
      return "Error: Division by zero!"
    else:
      return num1 / num2
  else:
    raise ValueError("Invalid operation")

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
