'''Write a Python program to accept an integer and determine
 whether it is a palindrome using a `while` loop '''

num = int(input("Enter an integer: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")