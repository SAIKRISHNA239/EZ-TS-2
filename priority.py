students_grade=[]
students_grade.append((1,"sai"))
students_grade.append((4,"krishna"))
students_grade.sort(reverse=True)
print("yes")
print(students_grade)
students_grade.append((2,"sid"))
students_grade.sort(reverse=True)
students_grade.append((3,"akahay"))
students_grade.sort(reverse=True)
print("priority wise sorted ")
print(students_grade)
print("original queue")
while students_grade:
    print(students_grade.pop())