score = input("Enter Score: ")
try:
    scr=float(score)
except:
    print('Give the correct number')
    quit()
if scr < 1 and scr > 0:
    if scr>=0.9:
        print('A')
    elif scr>=0.8:
        print('B')
    elif scr>=0.7:
        print('C')
    elif scr>=0.6:
        print('D')
    else:
        print('F')
    
else:
    print('the entered number is not within the range')
