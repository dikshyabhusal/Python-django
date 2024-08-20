numbers =[1,5,9,6,89,2,1203,4,23,1,0,-1]
#list.sort()
#print(list)

sort_list = []
i=0
for number in numbers:
    for i in range(0,len(sort_list)-1):
        if number < sort_list[i]:
            sort_list.insert(i,number)
            break
    else:
        sort_list.append(number)
print("Sorted list:",sort_list)
