
print ("function infused file I/O")


date=(input("(Insert the date): "))
# queue =input("enter:")

# note=input("write a note to remind yourself who you were today: ")

# 1. save_note(filename, note) - saves a note to file
def write():
    with open ("note.txt", "a") as file :
        file.write(input("write a note for your futureself: ") + "\n")
        # file.write( note +"\n")


# 2. read_notes(filename) - reads all notes from file
def read():
    with open ("note.txt", "r") as file:
         print(file.read())


# 3. Main code - asks user to save or read
# def main():
#     while date != "quit":
        
#         queue =input("you wanna naot the note: ")
#         if date == "y":
#             write()
            
#         date = input("do you wanna read the note?")
#         if date == "y":
#             read()
#         date=input("do you wanna save another note or wanna quit (y/quit)")
        





