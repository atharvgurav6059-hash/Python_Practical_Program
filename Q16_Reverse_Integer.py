'''Write a Python program to accept an integer and 
reverse its digits using a `while` loop.'''


num = int(input("Enter an integer: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse =", reverse)