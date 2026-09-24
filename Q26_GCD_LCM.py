'''Write a Python program to accept two positive integers and calculate
 their GCD and LCM using iterative statements.'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# GCD
gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

# LCM
lcm = max(a, b)

while lcm % a != 0 or lcm % b != 0:
    lcm = lcm + 1

print("GCD =", gcd)
print("LCM =", lcm)