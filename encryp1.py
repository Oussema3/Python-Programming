line=input("enter the string to be encrypted : ")
num=int(input("how many letters you want to shift : "))
while num > 26:
    num = num -26
empty=""

for char in line:
    
    if char.isalpha() is True:
        empty=chr(ord(char)+num)
        
        print(empty, end = "")
    else:
        empty=char
        print(empty,end="")
        
