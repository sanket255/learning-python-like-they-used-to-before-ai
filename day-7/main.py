
print ("function infused file I/O")


# date=(input("(Insert the date): "))
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

# read()
# 3. Main code - asks user to save or read
def main():
    
    ask=0
    while ask !="quit":
        ask=input("what do you want to do with your note write(w)or save(s) / read(r) / quit the programme: ")
        if ask =="s" or ask == "w":
            write()
        elif ask=="r":
            read()
        elif ask=="quit":
            break
        ask=input("Do you want add anothe note or quit the programme? (y/quit): ")

main()




