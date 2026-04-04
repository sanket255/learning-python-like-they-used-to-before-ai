print ("try/except")

num1=0
num2=0
op=0
ask=0
def add (num1, num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

while ask!="quit":
    ask=input("Do you want to get a calculation done (y/quit)")
    while True:
        try:
            num1=int(input("Enter number 1 that you want to oparate on: "))
        except ValueError:
            print("is not a number dont you understand what a number is what are you a foid")
    # while True:
        try:
            num2=int(input("Enter number 2 that you want to oparate on: "))
            if num2==0:
                print("invalid input try another number")
                continue
            break
        
        except ValueError:
            print("is not a number dont you understand what a number is what are you a foid")

    # Ask for operation (+, -, *, /)
    while True:
        try:
            op=(input("Enter the oparater you want (+, -, *, /): "))
            if op in ["+", "-", "*", "/"]:
                print("Invalid input try (+, -, *, /): ")
                continue
            break
        except ValueError:
            print("is not a opareation dont you understand what a number is what are you a foid")

    
# Try to do the math

    if op == "+":
        result=add(num1,num2)
    elif op == "-":
        result=sub(num1, num2)
    elif op == "*":
        result=mul(num1, num2)
    elif op =="/":
        result=div(num1, num2)
    
    print(result)

# Catch errors (division by zero, invalid operation)
# Show result
# Ask if they want another calculation or quit
# while True:



# # def guess():
# while True:
     
#     try:
#         ask=int(input("Enter a number inthe range of 1-100: "))
#         if ask < 1 or ask > 100:
#             print("Invalid number try again: ")
#             continue
#         break
    
#     except ValueError:
#         print("Invalid value try a number")



# Ask for number 1 (use try/except to validate)
# Ask for number 2 (use try/except to validate)