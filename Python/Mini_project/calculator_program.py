ops = input("Enter a operator to execute the program (+, -, *, /): ")
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

match ops:
    case "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {round(result,2)}")
    case "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {round(result,2)}")
    case "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {round(result,2)}")
    case "/":
        result = num1 / num2
        print(f"{num1} / {num2} = {round(result,2)}")
    case _:
        print(f"{ops} is not valid. Please enter a valid operator (+, -, *, /)")
