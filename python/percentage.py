#WAP to take user input mark percentage and find their division
percentage = float(input("Enter your mark percentage : "))
if percentage>80 and percentage<=100:
    print("Distinction")
elif percentage>60 and percentage<=80:
    print("First Division")
elif percentage>50 and percentage <=60:
    print("Second Division")
elif percentage>40 and percentage <=50:
    print("Third Division")
else:
    print("Fail")


#Wap to take user input email and validate wheather it is corrent email or not

email = input("Enter your email: ")

if '@' in email and '.com' in email:
    print("this is correct email")

else:
    print("this is wrong email")
    


