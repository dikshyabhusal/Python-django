
#last qn

student_names = ['Alice', 'Bob', 'Charlie']
student_marks = [85, 92, 78]
students_marks = {}
total_marks = 0
for i in range(len(student_names)):
    name = student_names[i]
    mark = student_marks[i]
    students_marks[name] = mark
    total_marks += mark

average_marks = total_marks / len(student_marks)

print(f"Student Marks: {students_marks}",f"Average ={average_marks}")

