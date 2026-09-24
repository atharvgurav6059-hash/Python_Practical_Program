'''Write a Python program to accept an integer and calculate
 the sum and product of all its digits using a `while` loop.'''

num = int(input("Enter an integer: "))

sum = 0
product = 1

while num > 0:
    digit = num % 10

    sum = sum + digit
    product = product * digit

    num = num // 10

print("Sum of digits =", sum)
print("Product of digits =", product)