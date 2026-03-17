
# Easy Challenge
# Create a simple calculator:

# Ask the user for 2 numbers
# Ask them which operation (+, -, *, /)
# Do the math
# Print the result

# Hint: You'll need input() to get user data


print("welcome to the calculator") #greetings
#variable input 
a=int(input("insert the value number 1:" ))
b=int(input('insert the value number 2:' ))
c=input('insert the operation you wanna get done (+, -, *, /):' )
# computational process
if c== "+" : (print(a+b))
elif c == "-":(print(a-b))
elif c == "*":(print(a*b))
else: (print(a/b))


# Intermediate Challenge
# Temperature converter:

# Ask user to input a temperature in Celsius
# Convert it to Fahrenheit using the formula: (C × 9/5) + 32
# Print results
# Do this 5 times in a loop (so user can convert multiple temps without restarting)

# Hint: You'll need loops and variables


# print('temprature converter')

# for i in range(5): 
#     a=int(input("insert the temprature1:" ))
#     b=((a*9/5)+32)
#     print(b)
    
    
# Hard Challenge
# Grade calculator:

# Ask user to input 5 test scores
# Calculate average
# Based on the average, assign a grade (A=90+, B=80-89, C=70-79, etc)
# Print all scores, the average, AND the grade

# Hint: You'll need loops, conditionals (if/else), and basic math
# z=[]
# for i in range (5):
#     a = int(input('insert the marks: '))
#     z.append(a)
# c=int(sum(z))
# print(c)
# b=c/5
# print(b)

# if b>=90:
#         print("A+")
# elif b>=80:
#         print("A")
# elif b>=70: 
#         print("B+")
# elif b>=60:
#         print("B")
# elif b>=50:
#         print("C+")
# elif b>=35:
#         print("C")
# else :
#         print("F")

# print(z)