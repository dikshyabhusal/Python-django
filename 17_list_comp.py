items = [1,2,3,4,5,6,7,8,9,10]
#list_2 = [item for item in items if item%2==0]
#print(list_2)

#square of each item in list
#without list compression
square_1 =[]
for item in items:
    item = item ** 2
    square_1.append(item)

print(square_1)

#with list compression
square_2=[item**2 for item in items]
print(square_2)

#without
square_3 =[]
for item in items:
    item = item +1000
    square_3.append(item)

print(square_3)

#with list compression
square_4=[item+1000 for item in items]
print(square_4)


for item in items:
    if item%2 == 0:
        print(f"{item}even")
    else:
        print(f"{item}odd")

data = ["apple","ball","cat","dog","ball","cat"]
items=[]
for item in data:
    if item in items:
        pass
    else:
        items.append(item)
print(items)
