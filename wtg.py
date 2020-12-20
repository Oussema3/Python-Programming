age = int(input("what is your age ?"))
if age == 5:
    print("you should go to kindergarten")
elif age >= 6 and age <=17:
    grade = age -5
    print("you should go to {} grade ".format(grade))
elif age > 17:
    print("you should go to college")
else :
    print("not an age to study")
