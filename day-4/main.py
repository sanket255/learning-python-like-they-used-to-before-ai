print("password cheacker!!")


user_pw=input("enter the password to check it's strength: ")
pwlen=len(user_pw)


if pwlen < 8 :
    print(f"{pwlen}an 3 year old with basic social engineering can hack your password, level up!!!")
if user_pw.isdigit() == "true":
    print("better but still i can look up in your instagram account like its nothin!!")
if user_pw.isupper() == "true":
    print("so now you have some decent level of security stil hackable!!!")
if user_pw.isalpha() == "true":
    print("superduperunhackable af!!!")





