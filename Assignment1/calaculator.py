import math


op = input("Enter oprator + - * / sin log cot fac cos sqrt:")
if op == "sin" or op == "log" or op == "fac" or op == "cot" or op == "tan" or op == "sqrt" or op == "cos":
    a = float(input("Enter your  Number :"))
else:
    a = float(input("Enter your First Number :"))
    b = float(input("Enter your Second Number :"))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        result = "Not number"
    else:
        result = a / b
elif op == "sin":
    result = math.sin(a)
elif op == "log":
    result = math.log(a)
elif op == "sqrt":
    result = math.sqrt(a)
elif op == "cos":
    result = math.cos(a)
elif op == "tan":
    result = math.tan(a)
elif op == "fac":
    result = math.factorial(a)
elif op == "tan":
    result = 1 / math.tan(a)

print(result)