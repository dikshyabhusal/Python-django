#create list
#append data to list and print
#access list item using for loop

user_name = []

number = int(input("How many users do you want? "))

for i in range(number):
    name = input(f"Enter the name of user {i+1}: ")
    age = int(input(f"Enter the age of {name}: "))
    
    user_name.append({"name": name, "age": age})

for j in user_name:
    print(f"Name: {j['name']}, Age: {j['age']}")

