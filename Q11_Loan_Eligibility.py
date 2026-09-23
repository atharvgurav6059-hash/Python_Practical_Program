'''Write a Python program to accept a person's age, monthly income,
 and credit score and determine whether the person is eligible for
   a loan based on specified conditions.'''

age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
credit = int(input("Enter credit score: "))

if age >= 21 and income >= 25000 and credit >= 700:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")