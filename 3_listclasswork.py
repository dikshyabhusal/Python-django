num =[1,5,9,6,89,1203,4,23]

highest_num=0
for number in num:
    number=int(number)
    if number >highest_num:
        highest_num=number
    else:
        pass
print("Highest number is:",highest_num)