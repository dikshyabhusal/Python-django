subjects = ["Computer_Network", "DBMS", "Technical_Writing", "Java_Programming", "NetCentric_Computing"]

marks_dict = {} #used to store subject and marks

for subject in subjects:
    marks = int(input(f"Enter the marks obtained in {subject}: "))
    marks_dict[subject] = marks

total_marks = sum(marks_dict.values())
num_subjects = len(subjects)
percentage = (total_marks / (num_subjects * 60)) * 100

if percentage>80 and percentage <=100:
    division = "Distinction"
elif percentage > 70 and percentage <=80:
    division = "First Division"
elif percentage >60  and percentage <=70:
    division = "Second Division"
elif percentage >40 and percentage <=50:
    division = "Third Division"

else:
    division = "Fail"

print(f"\nTotal Percentage: {percentage:.2f}%")
print(f"Division: {division}")

