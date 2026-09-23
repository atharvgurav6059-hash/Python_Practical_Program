'''Write a Python program to accept a time duration in seconds 
and convert it into hours, minutes, and seconds.'''

seconds=int(input("enter duration:"))
hours=seconds//3600
seconds=seconds%3600

minutes=seconds//60
seconds=seconds%60

print(hours,"hour",minutes,"minute",seconds,"seconds")