#!/usr/bin/python3
largest = None
smallest = None
while True:
    nume = input("Enter a number: ")
    # the break statement in the beginning, try and except next so it avoids the print invalid input again.
    if nume == "done" : 
        break
    try:
        num=int(nume)
    except:
       # print("Invalid input") # this print will print the output and continue
        err="Invalid input" # Displays the output at last, after the while loop gets completed with break.
    if largest is None:
        largest=num
    elif num>largest:
        largest=num
    if smallest is None:
        smallest=num
    elif num<smallest:
        smallest=num
print(err) # Printing at last, the except values.
print("Maximum is", largest)
print("Minimum is", smallest)
