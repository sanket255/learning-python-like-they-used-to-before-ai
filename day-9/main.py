print ("try/except")

# def guess():
while True:
     
    try:
        ask=int(input("Enter a number inthe range of 1-100: "))
        if ask < 1 or ask > 100:
            print("Invalid number try again: ")
            continue
        break
    
    except ValueError:
        print("Invalid value try a number")
        