ask="0"
print ('Build a Robust Input Validator:')

# Takes integer input. Catches:
while ask!="quit":
    try:
        user_input=int(input("Enter a number:"))    
        # break
    # ValueError (if user enters text)
    except ValueError:
        print("Enter a number!!!")
    # Handles it gracefully (asks again)
        continue
    # Loops until valid
    ask=input("Want to save another number? (y/quit): ")


while True:
    try:
        user_input=int(input("Enter a number:"))    
        break
    # ValueError (if user enters text)
    except ValueError:
        print("Enter a number!!!")
    # Handles it gracefully (asks again)
        continue
    # Loops until valid