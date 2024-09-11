set1 =set()
set2 =set()

for i in range(5):
    set1.add(i)
for j in range(3,9):
    set2.add(j)
set3= set1 & set2
print(set3)

