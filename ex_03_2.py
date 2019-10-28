hour=input("Enter the hrs worked:")
rate=input("Enter the rate charged:")
try:
    hf=float(hour)
    rf=float(rate)
except:
    print('Enter the valid numbers')
    quit()
if hf>40 :
    print('Overtime hrs:', hf-40)
    ohrs=hf-40
    opay=ohrs*(rf*0.5)
    regpay=hf*rf
    print('Wages', regpay+opay)
else :
    regpay=hf*rf
    print('Wages', regpay)
