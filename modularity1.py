#function lambda

yuuhuu = lambda:print("Good morning")
yuuhuu()


ttc = lambda prixHT:prixHT+ (prixHT * 20 / 100)
print(ttc(24))

#sum of two numbers 
calculer = lambda a,b : a+b
print(calculer(14,27))

"""
we will talk here about modularity

"""
from math import sqrt
from math import sin 
# the ex line will allow us to do a lot of mathematical functions
# it s something simular to include in C language  
resultat = sqrt(100) 
print(resultat)

"""
importer un module : import <nom_module>
                        or
                     from <nom_module> import <nom_function>
                     or
                     from <nom_module> import *
"""

sinus =sin(42)
print(sinus)
# Note that when u import u like importing a file that containthe functions that u will need 
# We can create our file (something simulat to the header in the C programming language)
"""
import os
os.system("cls")
"""
#this code will show the terminal 


import player
player.good_bye()
player.parler("Oussema","Hello cosomos")
