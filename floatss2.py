letter_z = "z"
num_3 = "3"
a_space= " "
def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False
print("is Pi a float: ",isfloat(num_3))
