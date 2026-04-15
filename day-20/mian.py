    # Build a 
print("Simple Personal Finance Tracker")
ask="0"
    # Add income/expense entries
while ask!="quit":
    try:
        date=input("whats the date today: ")
        user_income=int(input("Enter your total income: "))
        t_ex=int(input("how many expenses are there"))
        for user_expence in range(t_ex):
            user_expence=int(input("Enter your total expence: "))
        # for user_category in range(t_ex):
            user_category=input("enter for what you spent the money: ")
    except ValueError:
        print("Invalid input try a Number")
    # Save to file (date: amount: category format)

    with open ("asdf.txt","a") as file:
        file.write(f"{date}: {user_income}: {user_category}: {user_expence}")
    with open ("asdf.txt", "r") as file:
        print(file.read())

    # View balance (income - expenses)
    # saving=user_income-user_expence
    # print(saving)

    # View by category
    with open  ("asdf.txt", "r") as file:
        keyword=input("find through you expence: ")
        for line in file:
            if keyword in line:
                print(line)
    ask=input("do you want to add another listing(y/quit): ")

# Loop until quit
