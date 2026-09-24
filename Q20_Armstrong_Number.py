#Write a Python program to accept an integer and determine whether it is an Armstrong number.

num = int(input("Enter an integer: "))

original = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")