numbers = [1, 5, 9, 6, 89, 1203, 4, 23, 1]
sort_list = []

for number in numbers:
    inserted = False
    for i in range(len(sort_list)):
        if number < sort_list[i]:
            sort_list.insert(i, number)
            inserted = True
            break
    if not inserted:
        sort_list.append(number)

print("Sorted list:", sort_list)
