'''Write a Python program to accept the price and quantity of three products
 and calculate the subtotal, discount, GST, and final payable amount.'''

p1=float(input("enter price of product 1:"))
q1=int(input("enter quantity:"))
p2=float(input("enter price of product 2:"))
q2=int(input("enter quantity:"))
p3=float(input("enter price of product 3:"))
q3=int(input("enter quantity:"))

subtotal=(p1*q1)+(p2*q2)+(p3*q3)
discount=subtotal*10/100
amount=subtotal-discount
gst=amount*18/100
final_amount=amount+gst
print("subtotal",subtotal)
print("discount",discount)
print("gst",gst)
print("final payable amount",final_amount)

