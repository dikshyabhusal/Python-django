#WAP to make crud application for school.

student_data= []
while True:
    print("\n")
    print("******WELCOME TO SCHOOL APPLICATION")
    print("Enter 1 for register new student")
    print("Enter 2 for display all  student")
    print("Enter 3 for search student")
    print("Enter 4 for register update student")
    print("Enter 5 for resister delete student")
    print("Enter 6 if you want to exit? yes/no")
    choice = input("Enter your choice(1-6):")
    print("\n")

    if choice == '1':
        name=input("Enter you name:")
        roll_number=input("Enter you roll number:")
        age=input("Enter you age:")
        Grade=input("Enter your grade:")
        student ={"name":name,"roll_number":roll_number,"age":age,"Grade":Grade}
        student_data.append(student)
        print("Student Registered Successfully")
    
    elif choice =='2':
        if not student_data:
            print("No students registered yet")
        else:
            print("\n-------Registered Students list-------")
            for student in student_data:
                print(student)
    
    elif choice =='3':
        search_id = input("Enter the student roll numbet to search: ")
        for student in student_data:
            if student['roll_number'] == search_id:
                print("Congrats!!! Student found",student)
                break
            else:
                print("Student not found!")

    elif choice == '4':
        update_id =input("Enter student roll number to update.")
        for student in student_data:
            if student['roll_number'] == update_id:
                print(student)
                student['name'] = input("Enter new name: ")
                student['age'] = input("Enter new age: ")
                student['Grade'] = input("Enter new grade: ")
                print("Student information updated successfully!")
                break
            else:
                print("student not found")
            
    elif choice =='5':
        delete_id =input("Enter student roll number to delete")
        for student in student_data:
            if student ['roll_number'] == delete_id:
                student_data.remove(student)
                print(f"Student {roll_number} deleted successfully!!!")
                break
            else:
                print("Student not found")
                
    elif choice == '6':
        confirm_exit = input("Do you want to exit? (yes/no): ").lower()
        if confirm_exit == 'yes':
            print("Exiting the program...")
            break
        else:
            print("Continue with the program...")

    else:
        print("Invalid choice,Try again!!!.")