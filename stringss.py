rand_string ="     this is an important string      "
print(rand_string)
# get ride of the spacers from the left 
rand_string=rand_string.lstrip()
print(rand_string)

# get rid from the spaces of the right 
rand_string= rand_string.rstrip()
print(rand_string)

# get rid from all the spaces from left and from right 
rand_string = rand_string.strip()
print(rand_string)

#capitalise the first letter
print(rand_string.capitalize())

#uppercase the hole string
print(rand_string.upper())

#lowercase the whole string
print(rand_string.lower())

# print list separated with space or every thing you want to 
a_list=["bunch", "of","random","words"]
print(" ".join(a_list))

#
a_list2= rand_string.split()
for i in a_list2:
    print(i)
#count how many item in a line 
print("How many \"is\" :", rand_string.count("is"))

#find the index of a word in a string 
print("where is \"string\" ? :",rand_string.find("string"))

#replacing words in string
print(rand_string.replace("an ","a kind of "))
 
