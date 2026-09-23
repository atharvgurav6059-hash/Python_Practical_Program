'''Write a Python program to accept a student's percentage and display the appropriate grade 
using `if-elif-else` statements. Also validate that the percentage is between 0 and 100.'''

percentage=float(input("enter student percentage:"))
if percentage <0 or percentage >100:
    print("invalid percentage")
elif percentage>=80:
    print("First Grade")
elif percentage>=60:
    print("Second Grade")
elif percentage>=40:
    print("Third Grade ")
else:
    print("Fail")
    