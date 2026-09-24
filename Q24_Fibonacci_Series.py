'''Write a Python program to accept the number of terms and generate the Fibonacci
 series using a `for` loop. Also calculate the sum of the generated terms.'''

n = int(input("Enter number of terms: "))

a = 0
b = 1
sum = 0

for i in range(n):
    print(a, end=" ")

    sum = sum + a

    c = a + b
    a = b
    b = c

print()
print("Sum =", sum)

