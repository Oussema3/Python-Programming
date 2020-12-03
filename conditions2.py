#if elif 

age = input("please enter your age :")
age = int(age)
if age > 100:
    print("no such age haha")
    exit
else: 
    if age <= 13:
        print("you are a kid")
    elif age >13 and age < 18:
        print("You are a teenager") 
    elif age >= 18 and age < 27:
        print("You are young enough")
    elif age >= 27 and age < 50:
        print("you are adult")
    else:
        print("you are old ")
