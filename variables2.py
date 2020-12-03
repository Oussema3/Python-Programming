ame = input("choose a name for the player :")
print("the name of the palyer is : ", Name)



"""
viewed functions till now :

1 > print : print on screen 
2 > type : give the type of the variavble
3 > input : take data from user
4 > str.format : put the variables in the reserved space by {}
5 > int() : transfer the type of variable to int 
6 > float() : transform the type of data to a float type
7 > str() : transfer the type of data to a string type
8 > bool() ; transfer the type of data to a boolean type

"""

priceHT = input("print the price of the piece: ")

"""
we used the function int() in the above line because irt convert the data
entered from the user from string to integer because we 
will used the next line as an integer
"""
priceHT = int(priceHT)
priceTTC = priceHT + (priceHT * 20 / 100)
print("priceTTC is equal to : ",priceHT)



#exemple to changing the type of data from bool to int
#false will give a 0 instead of one

boolean_value = True 
boolean_value = int(boolean_value)
print(boolean_value)
