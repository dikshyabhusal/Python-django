name = "ram"
print(name.title())         #title(It print first lesson capital and other small as a title)
print(name.swapcase())      #swapcase(swap the lowercase to uppercase and viceversa)

text= "hello Friend"

print(text.upper())         #upper (Convert text into uppercase)
print(text.capitalize())    #capitalize(same as title does)
print(text.casefold())      #casefold (convert to lowercase)
print(text.isprintable())   #isprintable (returns true if strings are printable)

#join (join the letters with any operator indicated below)
girls=("isha","anusa","dikshya")
x="#".join(girls)
print(x)

#count(count the number of strings present there)
txt="I love coding,coding is my favorite"
y=txt.count("coding")
print(y)

#split(split the string and gives a list)
print(txt.split())


#strip (rstrip for right trim and lstrip for left trim)
abc="   hello   "
z=abc.rstrip()
print("everyone say",z,"To my brother")
z=abc.lstrip()
print("everyone say",z,"To my brother")

print(abc.split()) #split

#replace(Replace the strings)
fruits = "I like mango"

print(fruits.replace("mango", "apples"))

#zfill
txt = "50"

print(txt.zfill(3))



