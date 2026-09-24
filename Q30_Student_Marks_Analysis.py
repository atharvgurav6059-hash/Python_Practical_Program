'''Write a Python program to accept the marks of N students and calculate
 the class average, highest marks, lowest marks, number of passed and 
 failed students, and number of students scoring above 75%.'''

n = int(input("Enter number of students: "))

total = 0
highest = 0
lowest = 100
passed = 0
failed = 0
above75 = 0

for i in range(n):
    marks = float(input("Enter marks: "))

    total = total + marks

    if marks > highest:
        highest = marks

    if marks < lowest:
        lowest = marks

    if marks >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

    if marks > 75:
        above75 = above75 + 1

average = total / n

print("Class Average =", average)
print("Highest Marks =", highest)
print("Lowest Marks =", lowest)
print("Passed =", passed)
print("Failed =", failed)
print("Above 75% =", above75)