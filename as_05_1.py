largest = None
smallest = None
while True:
    nume = input("Enter a number: ")
    # the break statement in the beginning, try and except next so it avoids the print invalid input again.
    if nume == "done" : 
        break
    try:
       # nume=int(nume) # Fault that different varaible should be used else a traceback error will be continued.
        num=int(nume)
    except:
        err="Invalid input"
    if largest is None:
        largest=num
    elif num>largest:
        largest=num
    if smallest is None:
        smallest=num
    elif num<smallest:
        smallest=num
print(err)
print("Maximum is", largest)
print("Minimum is", smallest)