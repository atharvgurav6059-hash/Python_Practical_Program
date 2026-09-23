'''Write a Python program to accept a year and determine whether
 it is a leap year using relational and logical operators.'''

year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")