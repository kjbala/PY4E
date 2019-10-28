tot=0.0
num=0
while True:
    val=input('Enter the Number: ')
    if val=='done':
        break
    try:
        val=float(val)
    except:
        print('Invalid Entry')
        continue #used to avoid traceback since the datatype conversion uses same vname as the input.
        #continue # Used to avoid future traceback an optional one, its already avoided by using other vname cval
    num=num+1
    tot=tot+val
print(num,tot)

    