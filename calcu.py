print("Welcome to the calculator")

number_1 = float(input("first number"))
number_2 = float(input("second number"))
func = input("what math you wanna do")

if func == "+":
    plus = number_1 + number_2
    print(plus)
elif func == "-":
    minus = number_1 - number_2
    print(minus)
elif func == "*":
    multiply = number_1 * number_2
    print(multiply)
elif func == "/":
    divide = number_1 / number_2
    print(divide)
else:
    print("Upgrade your damn calculator! I quit!!")