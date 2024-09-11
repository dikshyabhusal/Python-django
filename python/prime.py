number=int(input("Enter a number to check it is prime or composite"))

if number <=1:
    print("number is neither prime nor composite")
else:
    for i in range(2, int(number)+1):
        if number % i ==0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("composite number")
def check_prime_composite(number):
    if number <= 1:
        return "Neither prime nor composite"
    elif number == 2:
        return "Prime"
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return "Composite"
        return "Prime"

# Example usage
num = 29
result = check_prime_composite(num)
print(f"{num} is {result}.")




def check_prime_composite(number):
    if number <= 1:
        return "Neither prime nor composite"
    elif number == 2:
        return "Prime"
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return "Composite"
        return "Prime"

# Take user input
num = int(input("Enter a number: "))
result = check_prime_composite(num)
print(f"{num} is {result}.")





