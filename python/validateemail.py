#Wap to take user input email and validate wheather it is corrent email or not

email = input("Enter your email: ")

if '@' in email and '.com' in email:
    print("this is correct email")

else:
    print("this is wrong email")
    