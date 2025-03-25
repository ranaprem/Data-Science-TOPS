def calculate():
  """A simple calculator."""

  print("Simple Calculator\nOperations: +, -, *, /")

  try:
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator: ")

    if operator == '+':
      result = num1 + num2
    elif operator == '-':
      result = num1 - num2
    elif operator == '*':
      result = num1 * num2
    elif operator == '/':
      if num2 == 0:
        print("Error: Division by zero") #division by zero error
        return
      result = num1 / num2
    else:
      print("Error: Invalid operator") #invalid operator error
      return

    print("Result:", result)

  except ValueError:
    print("Error: Invalid input (numbers only).") #invalid input error

calculate()