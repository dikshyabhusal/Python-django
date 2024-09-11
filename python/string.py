name = "ram"
print(name.title())         #title(It print first lesson capital and other small as a title)
#output Ram
print(name.swapcase())      #swapcase(swap the lowercase to uppercase and viceversa)
#output RAM

text= "hello Friend"

print(text.upper())         #upper (Convert text into uppercase)
#output HELLO FRIEND
print(text.capitalize())    #capitalize(same as title does)
#output Hello friend
print(text.casefold())      #casefold (convert to lowercase)
#output hello friend
print(text.isprintable())   #isprintable (returns true if strings are printable)
#output True

#join (join the letters with any operator indicated below)
girls=("isha","anusa","dikshya")
x="#".join(girls)
print(x)
#output isha#anusa#dikshya

#count(count the number of strings present there)
txt="I love coding,coding is my favorite"
y=txt.count("coding")
print(y)
#output 2

#split(split the string and gives a list)
print(txt.split())
#output ['I', 'love', 'coding,coding', 'is', 'my', 'favorite']

#strip (rstrip for right trim and lstrip for left trim)
abc="   hello   "
z=abc.rstrip()
print("everyone say",z,"To my brother")
#output everyone say    hello To my brother
z=abc.lstrip()
print("everyone say",z,"To my brother")
#output everyone say hello    To my brother

print(abc.split()) #split
#output ['hello']

#replace(Replace the strings)
fruits = "I like mango"
print(fruits.replace("mango", "apples"))
#output I like apples

#zfill
txt = "50"

print(txt.zfill(3))
#output 050


data="i love veg food"
print(data.replace("veg","non-veg"))

email="abc@gmail.com"
split_data=email.split('@')
second_part=split_data[1]
split_second_part=second_part.split('.')
print(split_second_part)


data="    how are you"
print(data.strip())