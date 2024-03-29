number1 = int(input("Enter your Number : "))
number2 = int(input("Enter your Number : "))
number3 = int(input("Enter your Number : "))

if number1 < number2 + number3 and number2 < number1 + number3 and number3 < number1 + number2:
    print("Ok you can")
else:
    print("no you cant")