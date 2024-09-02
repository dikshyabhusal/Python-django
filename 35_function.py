def convert_to_int(first_arg):
    int_data = int(first_arg)
    return int_data

def check_odd_even(value):
    if value % 2 ==0:
        return True
    else:
        return False 


input_number =input("Enter a number:")
output = convert_to_int(input_number)
check_odd_even_output = check_odd_even(output)
if check_odd_even_output == True:
    print("It is even")
else:
    print("It is odd")