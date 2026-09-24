'''Write a Python program to accept an integer and find the number of
 digits, largest digit, and smallest digit using a `while` loop.'''

num = int(input("Enter an integer: "))

count = 0
largest = 0
smallest = 9

while num > 0:
    digit = num % 10

    count = count + 1

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    num = num // 10

print("Number of digits =", count)
print("Largest digit =", largest)
print("Smallest digit =", smallest)