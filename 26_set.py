data={1,5,7,9,4,7}
data.add("apple")
print(data)


name ={"Diks","jigs","ish","ram","ankit"}
people ={"Laxman","ankit"}
vampires ={"diya","raju"}

new =name.union(people)
print(new)

popu = people | vampires
print(popu)

item= name.intersection(people)
print(item)