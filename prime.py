number=int(input("Enter a number to check it is prime or composite"))

if number <=1:
    print("number is neither prime nor composite")
else:
    prime = True

    for i in range(2, int(number / 2)+1):
        if number % i ==0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("composite number")





