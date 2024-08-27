first_tuple =("mathema","python","c++")

modified_list=[]
for i in first_tuple:
    first_tuple = i + "tics"
    modified_list.append(first_tuple)

modify_tuple =tuple(modified_list)
print(modify_tuple)
