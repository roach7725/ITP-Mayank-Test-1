def takeInput():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (+,-,*,/): ")
    return num1, num2, operator

def displayResult():
    num1, num2, operator = takeInput()

    if operator == "+":
        result = num1 + num2
        formula = f"{num1} + {num2} = {result}"
    elif operator == "-":
        result = num1 - num2
        formula = f"{num1} - {num2} = {result}"
    elif operator == "*":
        result = num1 * num2
        formula = f"{num1} * {num2} = {result}"
    elif operator == "/":
        result = num1 / num2
        formula = f"{num1} / {num2} = {result}"
    else:
        print("Invalid operator!")
        return

    print(formula)

displayResult()