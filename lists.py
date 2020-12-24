import math
import random
randList = ["string", 1, 1.26,"c"]
onToTen = list(range(10))

# in ppython we can combine several lists like the exemple above
randList = randList + onToTen 
print(randList)

# of course also we can manipulate and get data from lists using "print" and other functions

print(randList[12])
print(randList[0])
print("the length of this list is : ",len(randList)) 
first3 = randList[0:3]
print("the first three items of the list is : {}".format(first3))


for i in first3:
    print("{} : {}".format(first3.index(i),i))


print((first3[0] + " ") * 3)


# check wheter if something is inside a list 
print("string" in first3)

# get the index of a string in a list

print("index of \"string\" is :",first3.index("string"))

# find out how many times a variable apeears in a list 
print("how many time \"string\" apears in the list ? : ",first3.count("string"))

# changing lists items 
first3[0] = "new string"

# put another item at the end of the list using append 

first3.append("another list")
print(first3, end = " ")
