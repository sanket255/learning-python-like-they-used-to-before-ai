# ---------------------------------DAY-2---------------------------------------------------------
import random

print("guess the number type siii....")

numgen=random.randint(1,100)
print(numgen)
guess= 0
guess_list= []
guess_taken = 0

while guess!=numgen:
    
    guess=int(input("guess the number from 1-100:" ))
    guess_list.append(guess)
    guess_taken +=1
    if guess==numgen:
        print(f'{guess} {"good boiii why dont you try counting card next time"}')
    elif  guess>=numgen:
        print("too optimistic low the bar a bit:" )
    elif guess<=numgen:
        print("why so gloomy its not like we are asking to score your appereance here:" )
    # 
# 
# print(guess_list,guess_taken)
# 



# same problem solved using for loop 
# guess_list=[]

# for guess in range(numgen):
#     guess=int(input("guess the number from 1-100:" ))
#     guess_list.append(guess)
#     if guess==numgen:
#         print(f'{guess} {"good boiii why dont you try counting card next time"}')
#     elif  guess>=numgen:
#         print("too optimistic low the bar a bit:" )
#     elif guess<=numgen:
#         print("why so gloomy its not like we are asking to score your appereance here:" )

# print(f'{guess_list}, "your attempts lokey you suck..."')




# --------------------------------------DAY-3_stuff-----------------------------------------



# print("smart calculatior")

# number1=0
# number2=0

# while number2==number1:
#     number1=int(input("input the number 1:" ))
#     number2-int(input("input the number 2:" ))
#     op=input("what aperationyou wanna do ( +, -, *, / ):" )
#     if op == '+':
#         print(number1+number2)
#     elif op == '-':
#         print(number1-number2)
#     elif op == '*':
#         print(number1*number2)
#     elif op == "/":
#         print(number1/number2)

#     ask=input("do you want to do another calculation? (y/quit): ")
#     # if ask=="y":
#     #     print