data ="45678"
lowest_num =99999

for number in data:
    number=int(number)
    if number< lowest_num:
        lowest_num =number
    else:
        pass
print("Lowest number is",lowest_num)
