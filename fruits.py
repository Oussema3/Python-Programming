ruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#the code above will print apple and banana

for x in fruits:
  if x == "banana":
    break
  print(x)
  
# this code will oprint only apple because it will --
# break the statement when he reach the condition diorectly

for x in fruits:
  if x == "banana":
    continue
  print(x)
# in this code it will print apple then exit then print cherry

for x in range(6):
  print(x)
  
#this code will print numbers from 0 to 5 (6 elements)
for x in range(2, 30, 3):
  print(x)
else:
  print("I am out of the loop")
#this code will print from 2 to 3O range by 
#incrementing three per each execution
#for the code 
#: 2-5-8-11-14-17-20-23-27 
#and then go to the else that belogs to the for loop 
#Note : there is else to a for loop in python  


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

"""
OUTPUT :
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""
