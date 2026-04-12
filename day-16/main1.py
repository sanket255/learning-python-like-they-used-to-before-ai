    # task 2 

    # Ask user for filename
while True:
    try:
        a=input("Enter the name of the file: ") 
        # with open (f"{a}.txt", "a") as file:
        #     file.write(input("enter the notes you wanna save:")+"\n")

        # Try to open and read it
        with open (f"{a}.txt", "r") as file:
            print(file.read())
        break

    # Catch specific errors:

    # FileNotFoundError (file doesn't exist)

    except FileNotFoundError:
        print("file doesnt exist!")

        # IOError (can't read file)
    except IOError:
        print("cant open the file!!")
        # Generic Exception (anything else)
    except Exception as e:
        print (f"The error occur:{e}")
    # continuem
        # 
        # Handle each gracefully
        # Loop until quit