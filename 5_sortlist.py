numbers =[1,5,9,6,89,2,1203,4,23,1,0]
#list.sort()
#print(list)

sort_list = []
for number in numbers:
    for i in range(len(sort_list)):
        if number <sort_list[i]:
            sort_list.insert(i,number)
            break
    else:
        sort_list.append(number)
print("Sorted list:",sort_list)
