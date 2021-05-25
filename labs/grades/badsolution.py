# Lab Grades 
# Maira Kotsovoulou
grade = input("Type your numberic grade from 0 to 100\n")
# Cast grade to integer
grade = int(grade)
# Perform checks
if grade >= 0 and grade < 60:
    print("F")
if grade >= 60 and grade < 70:
    print("D")
if grade >= 70 and grade < 80:
    print("C")
if grade >= 80 and grade < 90:
    print("B")
if grade >= 90 and grade <= 100:
    print("A")
