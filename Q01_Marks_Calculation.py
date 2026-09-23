'''Write a Python program to accept the marks obtained by a student in five
 subjects and calculate the total marks, average marks, and percentage.'''

m1=float(input("Enter marks of subject 1:"))
m2=float(input("Enter marks of subject 2:"))
m3=float(input("Enter marks of subject 3:"))
m4=float(input("Enter marks of subject 4:"))
m5=float(input("Enter marks of subject 5:"))

total= m1+m2+m3+m4+m5
average=total/5
percentage=(total/500)*100
print("total marks of student is:",total)
print("average of student is:",average)
print("percentage of student is:",percentage,"%")