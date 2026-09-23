'''Write a Python program to accept marks obtained in Mathematics, 
Physics, and Chemistry and determine whether a student is eligible
for admission based on subject-wise and overall percentage requirements.'''

math = float(input("Enter Mathematics marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = math + physics + chemistry
percentage = total / 3

if math >= 50 and physics >= 50 and chemistry >= 50 and percentage >= 60:
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")

print("Percentage =", percentage)