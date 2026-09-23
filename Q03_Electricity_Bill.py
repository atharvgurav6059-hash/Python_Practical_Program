'''Write a Python program to accept the number of electricity units consumed by a consumer
 and calculate the electricity bill according to different consumption slabs.'''

units=int(input("Enter Units:"))

if units<=100:
    bill=units*2
elif units<=200:
    bill=units*3
elif units<=300:
    bill=units*5
else:
    bill=units*7
    
print("Electricity Bill:",bill)
