print("functions")

a=int(input("Enter the number 1 that you want to oparate: "))
b=int(input("Enter the number 2 that you want to oparate: "))
c=input("Enter the oparator that you want to oparate (+, -, *, /): ")

def add (a, b):
    return a + b

def sub (a, b):
    return a - b

def mul (a, b):
    return a * b

def div (a, b):
    if b==0:
        return "Error:cannot divide by 0"
    else:
        return a / b

def calculator(a,b,c):
    
    if c=="+":
       return add(a,b)
    elif c=="-":
        return sub(a,b)
    elif c=="*":
        return mul(a,b)
    elif c=="/":
        return div(a,b)

result= calculator(a,b,c)
print(f"the result is: {result}")
