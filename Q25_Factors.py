'''Write a Python program to accept an integer and display all its factors.
 Also display the total number of factors.'''

num=int(input("enter any number:"))
factors=0
for i in range(1,num +1):
    if num % i==0:
        print(i)
        factors=factors + 1
print("total number of counts:",factors)
