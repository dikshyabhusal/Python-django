
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
while True:
        choice = input("Enter choice(1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4','5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1 + num2)

            elif choice == '2':
                print(num1 - num2)

            elif choice == '3':
                print(num1 * num2)

            elif choice == '4':
                print(num1 / num2)
            
            elif choice =='5':
                print(num1 % num2)

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation != 'yes':
                break
        else:
            print("Invalid Input")

