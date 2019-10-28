hour=input("Enter the hrs worked:")
rate=input("Enter the rate charged:")
hf=float(hour)
rf=float(rate)
if hf>40 :
    print('Overtime hrs:', hf-40)
    ohrs=hf-40
    opay=ohrs*(rf*0.5)
    regpay=hf*rf
    pay=regpay+opay
    
else :
    pay=hf*rf

print('Wages',pay)
