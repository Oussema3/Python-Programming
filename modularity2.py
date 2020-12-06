"""
Module of the player

"""
def parler(person, message):
    print("{} : {}".format(person,message))

def good_bye():
    print("Good bye :) !")


# we will import this file in the modularity file
"""
we can add a test phase to see if this file is working good 
or not
this is done by this condition

"""

if __name__ == "__main__":
    print("PHASE DE TEST DE modularity2.py")

    parler("Jason ", "Good morning cosmos")
    au_revoir()
