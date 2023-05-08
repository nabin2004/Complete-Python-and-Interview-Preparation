def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculator():
    num1 = float(input("input number 1: "))
    num2 = float(input("input number 2: "))
    operation = input("Select an operator * for multiplication, - for subtraction, + for addition, / for division : ")

    if operation == "+":
        result = add(num1, num2)
        explanation = f"Adding {num1} and {num2} = {result}"
    elif operation == "-":
        result = subtract(num1, num2)
        explanation = f"Subtracting {num2} from {num1} = {result}"
    elif operation == "*":
        result = multiply(num1, num2)
        explanation = f"Multiplying {num1} by {num2} = {result}"
    elif operation == "/":
        result = divide(num1, num2)
        if type(result) == str:
            explanation = result
        else:
            explanation = f"Dividing {num1} by {num2} = {result}"
    else:
        explanation = "Invalid operation"
        result = None

    return explanation

print(calculator())
