"""
viewed functions :
print() : print 
input() : get data from user
type()  :givr the type of variable 
int(),float,bool(),str() : change tytpe of variable

"""

age = input("Quelle age a tu ?")
age = int(age)
print("vous avez {} ans".format(age))


"""
to create a function u have to follow the same 
syntaxe of creatiing a variable (no special character no spaces ..etc)
begin defining the function with the key word      ::::     """"def""""
"""


def say_GM():
    print("Good morning :) !")
# I am not in the function right now 
# I am going to cdall the function in the above code 
say_GM() 


# Function with parametres

def tell(name, message):
    print("{} : {}".format(name,message))


tell("oussema","waaaa klauud")
tell("khaled","wa round")


"""
we can set the data for the arguments from the begining exemple :
#     def tell(name="Oussema",message = "hello cosmos")
"""

# we can have an infinite number of aarguments inside a function 

def roundd(*list_of_items):
    for item in list_of_items:
        print(item) 
#now i am out of the function and i ll call it 

roundd("hey","Jude","don't","be","Afraid")
roundd("Take","a","bad","song","and","make","it","Better")

#this a function tha makes the sum of 3 numbers

def summ(first_num,second_num,third_num):
    return first_num + second_num + third_num
     
print(summ(7,13,20))

# this is a function that returns the biggest number
def bigg(numm1,numm2):
    
    if numm1 - numm2 == 0:
        return numm1
    elif numm1 - numm2 < 0:
        return numm2
    else :
        return numm1 
#now out of "bigg" function and i am calling it to compare 2 numbers
print("the biggest number is: {} ".format(bigg(6,100)))
