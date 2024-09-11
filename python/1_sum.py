sum = 0
for i in range(1,10):
    number =int(input(f"Enter {i+1} numbers:"))
    if i == 4:
        break
    sum =sum+number
print("Sum is",sum)

print("\n")

sum = 0
for i in range(5):
    number =int(input(f"Enter {i+1} numbers:"))
    if number%2 == 0:
        pass
    sum =sum+number
print("Sum is",sum)

print("\n")

sum = 0
for i in range(10):
    number =int(input(f"Enter {i+1} numbers:"))
    if number == 0:
        break
    sum =sum+number
print("Sum is",sum)

