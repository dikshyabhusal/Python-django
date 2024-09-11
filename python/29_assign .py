#program to find odd or even number  using function
def odd_or_even(number):
        if number %2==0:
            print("even number")
        else:
            print("odd number")
num = int (input("Enter a number to check it is odd or even:"))
result= odd_or_even(num)



