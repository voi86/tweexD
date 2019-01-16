largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        f=float(num)
        
        
    except:
        print("Invalid Input")
        
    
    if smallest is None :
        smallest = f
    elif smallest> f :
        smallest = f
        

    if largest is None :
        largest = f
    elif largest< f :
        largest = f
    
        

print("Maximum is ", int(largest))
print("Minimum is ", int(smallest))