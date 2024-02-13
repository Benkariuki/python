# calculator program
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

    # taking input from the user


num1 = float(input("Enter first number"))
operator = input("Enter your operator(+,-,/,*):")
num2 = float(input("Enter second number"))
# performing calculations based on the operator
if operator == "+":
    print(num1 + num2)
if operator == "-":
    print(num1 - num2)
if operator == "/":
    print(num1 / num2)
if operator == "*":
    print(num1 * num2)
