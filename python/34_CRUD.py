student_data = []

def register_student():
    name = input("Enter Name: ")
    roll_num = input("Enter Roll Number: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    student = {"name":name , "roll_num":roll_num,"age":age ,"grade": grade }
    student_data.append(student)
    print(f"Student {name} registered successfully!!!")

def display_student():
    if not student_data:
        print("NO student registered yet.")
    else:
        print("---Student registered list---")
        for student in student_data:
            print(student)

def search_student():
    roll_num =input("Enter roll number you want to search")
    for student in student_data:
        if student['roll_num'] == roll_num:
            print("Congratulations!!!Student found successfully",student)
            break
        else:
            print("Student not found!!")

def update_student():
    roll_num =input("Enter roll number of a student whose information you are going to update")
    for student in student_data:
        if student['roll_num'] == roll_num:
            name =input("Enter new name:")
            age = input("Enter new age:")
            grade = input("Enter new grade:")
            if name:
                student['name'] = name 
            if age:
                student['age'] = age
            if grade:
                student['grade'] =grade
            print(f"Student with {roll_num} updated successfully")
        else:
            print(f"Student with {roll_num} not found")


def delete_student():
    roll_num = input("Enter roll number to delete.")
    for student in student_data:
        if student['roll_num'] == roll_num:
            student_data.remove(student)
            print(f"Student with Roll Number {roll_num} deleted successfully!")
        else:
            print(f"Student with Roll Number {roll_num} not found.")


def menus():
    print("******WELCOME TO SCHOOL APPLICATION")
    print("Enter 1 for register new student")
    print("Enter 2 for display all  student")
    print("Enter 3 for search student")
    print("Enter 4 for register update student")
    print("Enter 5 for resister delete student")
    print("Enter 6 if you want to exit? ")
    print("\n")

while True:
    menus()
    choice =input("Enter your choice from (1-6) : ")
    if choice == '1':
        output = register_student()
    elif choice == '2':
        output = display_student()
    elif choice == '3':
        output = search_student()
    elif choice == '4':
        output = update_student()
    elif choice == '5':
        output = delete_student()
    elif choice == '6':
        print("Existing the program...")
        break
    else:
        print("Invalid parameter")
print(output)