def calculator():
  while True:
    try:
      num =input("Enter the first number (or 'q' to quit): ")
      if num == 'q':
        print("Thank You")
        break
      else:
          num1 = float(num)

      num2 = float(input("Enter the second number: "))
      operator = input("Enter an operator (+, -, *, /, ^, %): ")

      if operator not in "+-*/^%":
        print("Invalid operator. Please use +, -, *, /, ^, or %.")
        continue

      if operator == "+":
        result = num1 + num2
      elif operator == "-":
        result = num1 - num2
      elif operator == "*":
        result = num1 * num2
      elif operator == "/":
        if num2 == 0:
          print("Error: Division by zero is undefined.")
          continue
        else:
          result = num1 / num2
      elif operator == "^":
        result = num1 ** num2
      elif operator == "%":
        result = num1 % num2

      print("Result:", result)

    except ValueError:
      print("Invalid input. Please enter numbers for both values.")
      continue

# Call the calculator function
calculator()
