# Task 1 (Learning): 
# 
# 
print("File I/O Note Saver")


# # User enters notes
# # Saves to a file
start=input("ready to write a note to futureself?? ")


while start != "quit":
    with open ("notes.txt" , "a")as file:
        file.write(input("write a note for your futureself: ") + "\n")


    # Reads them back
    readin=input("do yuo wanna read what you have written so far?? (y/quit): ")
    if readin == "y":
        with open("notes.txt", "r") as file:
            print(file.read())


    # Can append new notes
    readin=input("do you wanna add another note to your future?? (y/quit) : ")
    if readin == "y":
        with  open("notes.txt", "a")as file:
            file.write(input("write a note to youre future self: ") +"\n")
    start=input("do you want to stop here or another note to future?? (y/quit) ")

































# with open("hero_name.txt", "w") as file:
#     file.write("Captain Python!")

# note=input("write the note for your future self: ")