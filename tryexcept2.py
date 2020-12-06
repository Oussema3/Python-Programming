number1 = 150

number2 = input("enter a number")

try:
    number2 = int(number2)
    print("Result is {}".format(number1/ number2))
except ZeroDivisionError:
    print("You can devide by zero")
except ValueError:
    print("enter a valid number")
else:
    print("Well done u have entered a valid value")
finally:
    print("program is done")
