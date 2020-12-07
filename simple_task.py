number = input("enter a number : ")
number = int(number)
result = 1
if number < 0 :
    print("the result is : 0") 
    exit()
    
elif number == 0 or number == 1:
    print('the result is : 1')
    exit()
else:
    while (number > 1):
        
        result *=number
        number = number - 1 
print("the result is {}".format(result))
