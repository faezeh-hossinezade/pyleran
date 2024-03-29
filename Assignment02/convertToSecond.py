import re
# The Python "re" module provides regular expression support. In Python a regular expression search is typically written as: match = re. search(pat, str)
# The re.search() method takes a regular expression pattern and a string and searches for that pattern within the string.
timee = input("Enter time (hh:mm:ss): ")

time_sp = re.split(':',timee)
hour = int(time_sp[0])
minute = int(time_sp[1])
second = int(time_sp[2])

converted_time = (hour * 3600) + (minute * 60) + second

print("convertedTOsecond : ",converted_time,"second")