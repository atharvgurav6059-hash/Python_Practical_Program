'''Write a Python program to accept an employee's basic salary and
 calculate DA, HRA, gross salary, tax deduction, and net salary.'''

basic=float(input("enter basic salary:"))
da=basic*10/100
hra=basic*20/100
gross=basic+da+hra
tax=gross*5/100
net=gross-tax

print("DA:",da)
print("HRA:",hra)
print("Gross Salary:",gross)
print("Tax Deduction:",tax)
print("Net Salary:",net)
