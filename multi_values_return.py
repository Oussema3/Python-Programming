def mult_divide (num1, num2):
    
    

        return (num1 * num2), (num1 / num2)
    
    

try:
    mult, divide = mult_divide(5, 0)
    print("5 * 0 = ",mult)
    print("5 / 0 = ",divide)
except ZeroDivisionError:
    print("you cant devide by zero")
