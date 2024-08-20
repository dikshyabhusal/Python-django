subject={"math":78,"science":56,"English":88,"Nepali":44}

for key in subject.keys():
    print(f"Your mark in {key} subject is {subject[key]}")

#WAP to ask subject and their mark and print their percentage and division
# Function to calculate percentage and division
def calculate_percentage_and_division(marks_dict):
    total_marks = sum(marks_dict.values())
    num_subjects = len(marks_dict)
    
    percentage = (total_marks / (num_subjects * 100)) * 100
    
    if percentage >= 60:
        division = "First Division"
    elif percentage >= 50:
        division = "Second Division"
    elif percentage >= 40:
        division = "Third Division"
    else:
        division = "Fail"
    
    return percentage, division

# Dictionary to store subject and marks
marks_dict = {}
num_subjects = int(input("Enter the number of subjects: "))

# Input marks for each subject
for _ in range(num_subjects):
    subject = input("Enter the subject name: ")
    marks = int(input(f"Enter the marks obtained in {subject}: "))
    marks_dict[subject] = marks

# Calculate percentage and division
percentage, division = calculate_percentage_and_division(marks_dict)

# Print results
print(f"\nTotal Percentage: {percentage:.2f}%")
print(f"Division: {division}")
