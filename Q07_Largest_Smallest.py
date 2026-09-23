'''Write a Python program to accept three numbers and determine the
 largest and smallest number using decision-making statements.'''

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if num1>num2 and num1>num3:
    largest= num1
elif num2>num1 and num2>num3:
    largest= num2
else:
    largest=num3
    
if num1<num2 and num1<num3:
    smallest= num1
elif num2<num1 and num2<num3:
    smallest= num2
else:
    largest=num3

print("Largest",largest)
print("Smallest",smallest)
    
    