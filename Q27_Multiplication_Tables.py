'''. Write a Python program using nested `for` loops to display multiplication
 tables from 1 to 10 in a structured tabular format.'''

for i in range(1, 11):
    print("Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print()