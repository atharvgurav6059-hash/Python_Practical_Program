'''Write a Python program to create a menu-driven mathematical application with
 options to check Prime, Palindrome, Armstrong, Factorial, Fibonacci Series, and
   Exit. The menu should be displayed repeatedly until the user selects Exit.'''

while True:
    print("\n1. Prime")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        n = int(input("Enter number: "))
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        print("Prime" if count == 2 else "Not Prime")

    elif ch == 2:
        n = int(input("Enter number: "))
        original = n
        reverse = 0

        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n = n // 10

        print("Palindrome" if original == reverse else "Not Palindrome")

    elif ch == 3:
        n = int(input("Enter number: "))
        original = n
        total = 0

        while n > 0:
            digit = n % 10
            total += digit ** 3
            n //= 10

        print("Armstrong" if total == original else "Not Armstrong")

    elif ch == 4:
        n = int(input("Enter number: "))
        f = 1

        for i in range(1, n + 1):
            f *= i

        print("Factorial =", f)

    elif ch == 5:
        n = int(input("Enter terms: "))
        a, b = 0, 1

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b

        print()

    elif ch == 6:
        print("Program Ended")
        break

    else:
        print("Invalid choice")