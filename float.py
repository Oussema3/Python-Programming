inves, expec =input("ammount of investment followed by expected interest: ").split()
inves = float(inves)
expec = float(expec) * .01
for i in range(10):

    inves = inves + (inves * expec)
    
print("after 10 years you will have {:.2f} ".format(inves))
