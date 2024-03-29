name = input("Enter your name :")
family = input("Enter your family :")

number1 = int(input("Enter your Number :"))
number2 = int(input("Enter your Number :"))
number3 = int(input("Enter your Number :"))

average = (number1 + number2 + number3) / 3

if average >= 17:
    print("Great")
elif average < 17 and average >= 12:
    print("Normal")
elif average < 12:
    print("Fail")