import re

statement = input("Enter your statement: ")
words = re.split(" ",statement)
print(len(words))