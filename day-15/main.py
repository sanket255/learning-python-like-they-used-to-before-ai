# Day 15 Real Task
# Build a program that:



print("advanced dictionary oprations!!!")



user_list=[]
num_list=[]

# c= int(input("How many contacts you wanna save: "))

for i in range(3):
# Takes user input (name: phone pairs)
    user_name=input("Enter user name: ")
    user_num=input("Enter user number: ")
    user_list.append(user_name)
    num_list.append(user_num)

# Stores them in a dictionary
dick=dict(zip(user_list,num_list))
# print(dick)
# Lets user choose: view names only / view numbers only / view both
ask ="0"
while ask!="quit":
    ask=input("do you only want to see names / only numbers / or both ( a / b / c / quit ):")
    if ask =="a":
        for key in dick.keys():
            print(key)
    elif ask == "b":
        for value in dick.values():
            print(value)
    elif ask == "c":
        print(dick)
# Loop until quit
    elif ask == "quit":
        print("bye bye!!!")
        break


