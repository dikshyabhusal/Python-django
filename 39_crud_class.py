class School:
    student_data = []
    def register_student(self):
        name = input("Enter Name: ")
        roll_num = input("Enter Roll Number: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        student = {"name":name , "roll_num":roll_num,"age":age ,"grade": grade }
        self.student_data.append(student)
        print(f"Student {name} registered successfully!!!")

    def display_student(self):
        if not self.student_data:
            print("NO student registered yet.")
        else:
            print("---Student registered list---")
            for student in self.student_data:
                print(student)

    def search_student(self):
        roll_num =input("Enter roll number you want to search")
        for student in self.student_data:
            if student['roll_num'] == roll_num:
                print("Congratulations!!!Student found successfully",student)
                break
            else:
                print("Student not found!!")

    def update_student(self):
        roll_num =input("Enter roll number of a student whose information you are going to update")
        for student in self.student_data:
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


    def delete_student(self):
        roll_num = input("Enter roll number to delete.")
        for student in self.student_data:
            if student['roll_num'] == roll_num:
                self.student_data.remove(student)
                print(f"Student with Roll Number {roll_num} deleted successfully!")
            else:
                print(f"Student with Roll Number {roll_num} not found.")


    def menus(self):
        while True:
            print("******WELCOME TO SCHOOL APPLICATION")
            print("Enter 1 for register new student")
            print("Enter 2 for display all  student")
            print("Enter 3 for search student")
            print("Enter 4 for register update student")
            print("Enter 5 for resister delete student")
            print("Enter 6 if you want to exit? ")
            print("\n")

            choice = input("Enter your choice:")
            if choice == '1':
                self.register_student()
            elif choice == '2':
                self.display_student()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print("Exiting the application!!!")
                break
            else:
                print("Invalid choice. Please try again.")


class_obj = School()
class_obj.menus()

