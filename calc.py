num1, operator,num2 = input("what is the operation that you wanna do ?").split()

num1= int(num1)
num2= int(num2)

if operator == '+':
    result = num1 + num2
    print("{} {} {} = {}".format(num1,operator,num2,result))
elif operator =='-':
    result = num1 - num2
    print("{} {} {} = {}".format(num1,operator,num2,result))
elif operator =='*':
    result=num1*num2
    print("{} {} {} = {}".format(num1,operator,num2,result))
elif operator =='%':
    result = num1 % num2
    print("{} {} {} = {}".format(num1,operator,num2,result))
else:
    print('please enter a valid expression')
    
