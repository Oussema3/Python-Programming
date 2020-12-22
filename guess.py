winn = 6

while True:
    try:
        num=int(input("Please guess a number betwwen 0 and 10 : "))


        if num==winn:
            print("nice guess you won !!!")
            break
        
        elif num < 0 or num > 10 :
            print("number out of range please guess again !")
            continue
        else:
            print("wrong please try again")
            continue

    except ValueError:
        print("please enter a number ")
    except:
        print("Unknown Error occured :( ")
