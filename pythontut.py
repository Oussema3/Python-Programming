# ask the user to input to vzlues them in variables num1 and num2 


#convert the strings into regular numbers 


# add the values entered and store in sum 
 
# subtract variable and store in deffirence 

# multiply the values and store in product 

# Divide the variables on the values to find the quotion

#

num1, num2=input("Enter 2 numbers").split()
num1 = int(num1)
num2 = int(num2)

sum= num1 + num2

print("{} + {} = {}".format(num1, num2, sum))

sub= num1 - num2
print("{} - {} = {}".format(num1, num2, sub))

prod= num1 * num2
print("{} * {} = {}".format(num1, num2, prod))

div= num1 // num2
print("{} / {} = {}".format(num1, num2, div))


rest= num1 % num2

print("{} % {} = {}".format(num1, num2, rest))
