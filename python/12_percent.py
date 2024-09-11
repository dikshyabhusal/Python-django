
total_student=[]
for j in range(1,3):
    subject_names={}
    total_marks =0

    student_name=input("Enter student name:")
    for i in range(1,3):
        sub_name =input("Enter subject name:")
        marks=int(input(f"Enter the marks obtained in {sub_name}: "))
        subject_names[sub_name] = marks
        total_marks= total_marks +  int(marks)
        percentage =(total_marks/500)*100

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

    subject_names['percentage']=percentage
    subject_names['Divsion']= division
    subject_names['student_name']=student_name

    total_student.append(subject_names)
print(total_student)

#give example of each 

#create list
#append data to list and print
#access list item using for loop

#create dictionary
#append data to dictionary and print
#how to access and change the value of dictionary
#access dictionary item using for loop

#add dictionary to list
#print mark and name using loop from data = [{'name':"salman",'percentage':45},{'name':"Mithun",'percentage':45}]