def is_prime(number):
    if number <=1 :
        return "Neither prime nor composite"
    else:
        for i in range(2, int(number)+1):
            if number%i ==0:
                return True
            else:
                return False
    
input_number = int(input("Enter a number to check it is prime or composite:"))
output = is_prime(input_number)
if output == True:
    print("It is Composite")
else:
    print("It is Prime")

