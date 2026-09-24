'''Write a Python program to accept two integers representing a range and display all prime 
numbers within that range. Also display the total number of prime numbers found.'''

start=int(input("Enter starting number:"))
end=int(input("Enter ending number:"))

count=0
for num in range(start, end + 1):
    factors=0
    for i in range(1, num + 1):
        if num % i==0:
            factors= factors + 1
    if factors ==2:
        print(num)
        count= count+1
print("Total prime numbers =", count)
        



