# print("smart calculatior")

# ask=input("do you want to do calculations? (y/quit):" )

# while ask !="quit":
#     number1=int(input("input the number 1:" ))
#     number2=int(input("input the number 2:" ))
#     op=input("what operation you wanna do? ( +, -, *, / ):" )
#     if op == '+':
#         print(number1+number2)
#     elif op == '-':
#         print(number1-number2)
#     elif op == '*':
#         print(number1*number2)
#     elif op == "/":
#         print(number1/number2)       
#     # if ask1 == "quit":



# --------------------------------------TASK-2-----------------------------------------


ask=input("do you want to do check palindromes? (y/quit):" )

while ask != "quit":
    user_input=input("input the word to check weather its a palindrome or not :" )
    input_r= user_input[::-1]
    if user_input != input_r:
        print (f"no the word {user_input} is not palindrome!")
    elif input_r == user_input :
        print(f"yes the word {user_input} is palindrome")

    ask=input("do you want to continue checking the palindrome words or youll channle this energy to find some job or something?? (y/quit) :" )







