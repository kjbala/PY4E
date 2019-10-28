def computepay(h,r):
    if h>40:
        opay=(h-40)*(r*0.5)
        rpay=h*r
        pay=opay+rpay
    else:
        pay=h*r
        
    return pay

hrs = input("Enter Hours:")
rate = input("Enter the Rate:")

p = computepay(float(hrs),float(rate))
print(p)