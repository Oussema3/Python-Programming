import math
import random

numList = []

for i in range(5):
    numList.append(random.randrange(1,9))

for i in numList:
    print(i,end =" ")


#sort the list 
numList.sort()
print()
print(numList)
#reverse the sorted list
numList.reverse()

print(numList)

#add the list an element in a predifined index

numList.insert(1,"Hey jude")
print(numList)

#remove an item from a list with a specific index

numList.pop(3)
print(numList)

#remove an item from a list 
numList.remove("Hey jude")
print(numList)
