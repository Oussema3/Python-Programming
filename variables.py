
"""

nommer un variable
1:begins with a character 
2:dosent contain a special character
3:dosent contain spaces
4:use undersore _ to split words

types of variables : entier numerique (int)
float number : float 
string : chainesq de characteres
boolean = true and false 

"""
AgeOfPerson = 14
#this will be stocked  as integer

agePersonne2 = "26"
#this will be stored as a string


print(AgeOfPerson)
print(type(AgeOfPerson))

print(agePersonne2)
print(type(agePersonne2))


priceHt = 123.25

continuer_partie = False
print(priceHt)
print(type(priceHt))

print(continuer_partie)
print(type(continuer_partie))


#type is a function that give you the type of the variable 

#print handle more then one argument 

print("Age de la personne :" , AgeOfPerson, ".")
text = "the age of the person is {} and his price is {} $"
print(text.format(AgeOfPerson,priceHt))

#format ia a function that put the variables in the la place reserved for it by "{}"
#we can also use that 

print("the age of the person is {} and it's price is {}".format(AgeOfPerson,priceHt))


