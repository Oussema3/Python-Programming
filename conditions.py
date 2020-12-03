#testing forum exemple 






identifier = "Jason"
password = "Password123"
"""


operator conditions
1 > == : cthis is assigning and testing for equality
2 > != : this means not equal to
3 > ">": grater than
4 > "<": less  than
5 > => equal or greater
6 > =< equal or less
7 > and :  & in C language 
8 > or : || in C language
9 > "in" and "not in" as the same meaning if the english languge 
10 >



"""
user_id = input("Enter ur user identifier : \n")
 

if (user_id != identifier ):
    print("No such user name plz ry again",user_id)
else:
    user_password = input("Enter ur password : \n")
    if (user_password != password):
        print("please enter the correct password",user_id)
    else:
        print("you have logged in",user_id)




