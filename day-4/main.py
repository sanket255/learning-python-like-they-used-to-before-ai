print("password cheacker!!")

initi=input("do you wanna check password???: ")


while initi != "quit":
    strength=0
    user_pw=input("enter the password to check it's strength: ")
    for char in user_pw:
        if char.isdigit():
            strength+=1
            break
    for char in user_pw:
        if char.isupper():
            strength+=1
            break
    for char in user_pw:
        if char.isalpha():
            strength+=1
            break

    if strength < 2 :
        print("an 3 year old with basic social engineering can hack your password, level up!!!")
    if strength == 2 :
        print("your password is decent but hackable!!")
    if strength > 2 :
        print("fuk bro your password is SuperDuperUnHackable!!!!!")

    initi=input("do you wanna do another password check (y/quit): " )


