"""
synatax: Try/except (+ else,finally)

types of exceptions:
-ValueError
-NameError
-TypeError
-ZeroDivisionError
-OSError
-AssertionEroor


"""





age = input("what is ur age ")

try:
    age = int(age)
    print("You have ",age,"years old")
except:
    print("enter a valid age")
finally:
    print("Program done !")


    
