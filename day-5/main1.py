print("functions")

a=int(input("Enter the number 1 that you want to oparate: "))
b=int(input("Enter the number 2 that you want to oparate: "))
c=input("Enter the oparator that you want to oparate (+, -, *, /): ")

def add (a, b, c):
    if c == "+":
        print(a+b)

def sub (a, b, c):
    if c == "-":
        print (a-b)

def mul (a, b, c):
    if c == "*":
        print(a*b)

def div (a, b, c):
    if c == "/":
        print(a/b)

def calculator(add, sub, mul, div):
    add(a, b, c)
    sub(a, b, c)
    mul(a, b, c)
    div(a, b, c)

calculator(add, sub, mul, div)