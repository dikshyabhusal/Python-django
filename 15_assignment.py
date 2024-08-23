#create dictionary
#append data to dictionary and print
#how to access and change the value of dictionary
#access dictionary item using for loop

#create dictionary
User_name = {"Name": "Dikshya","Age": "21","District": "Chitwan"}
print(User_name)

#append data to dictionary and print
User_profile={"Name": "Dikshya","Age": "21","District": "Chitwan"}

User_profile["Country"]="Nepal"
User_profile["Class"]="Seventh Semester"

print(User_profile)


#how to access and change the value of dictionary


User_profile={"Name": "Dikshya","Age": "21","District": "Chitwan"}
print("Original name:",User_profile["Name"])
print("Original Age:", User_profile["Age"])  
print("Original District:", User_profile["District"])  

User_profile["Name"]="Ram"
User_profile["Age"] = "22" 
User_profile["District"] = "Kathmandu"  


print("Updated User_profile:", User_profile)

print("\n")


#access dictionary item using for loop

numbers ={}
for num in range(1,5):
    marks=int(input(f"Enter {num} number:"))
    numbers[num] =marks
total=sum(numbers.values())

print(f"\nTotal Sum:{total}")