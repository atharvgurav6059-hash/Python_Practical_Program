'''Write a Python program to accept monthly mobile data usage in GB and
 calculate the total bill according to specified usage slabs.'''


data = float(input("Enter data usage in GB: "))

if data <= 5:
    bill = data * 10

elif data <= 10:
    bill = data * 15

elif data <= 20:
    bill = data * 20

else:
    bill = data * 25

print("Total Bill =", bill)