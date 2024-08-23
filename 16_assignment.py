#add dictionary to list
#print mark and name using loop from data = [{'name':"salman",'percentage':45},{'name':"Mithun",'percentage':55},{'name':"Katrina",'percentage':34}]

data = []

# Create dictionaries and add them to the list
data.append({'name': 'salman', 'percentage': 45})
data.append({'name': 'Mithun', 'percentage': 55})
data.append({'name': 'Katrina', 'percentage': 34})



#using for loop
for i in data:
    print(f"Name: {i['name']}, Percentage: {i['percentage']}")


