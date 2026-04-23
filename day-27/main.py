class Calculator:
    def add(self,a,b):
        return a+b
    def sub (self,a,b):
        return a-b
    def mul (self,a,b):
        return a*b
    def div(self,a,b):
        if b == 0 :
            return("a number cant be divided by 0")
        else:
            return a/b
    

calc = Calculator()

while True:
    while True:
        try:
            num1 = int(input("Enter number 1: "))
            num2 = int(input("Enter number 2: "))
                
            break
        except ValueError:
            print ("either of them is not a number, try a number(1,2,3,4,....): ")
            continue
    opre = input("Enter the oparation ( +, - , * , / ) :")

    if opre == "+":
        result = calc.add(num1,num2)
    elif opre == "-":
        result = calc.sub(num1,num2)
    elif opre == "*":
        result = calc.mul(num1,num2)
    elif opre == "/":
        result = calc.div(num1,num2)

    print(result)
    ask = input("do you want another calc or (quit)?: ")
    if ask == "quit":
        break