# Day 8 Task: Combine Everything


# Build 
# with Full Features:
# 
print('a Personal Journal App')

# Save entries with date (use file I/O + functions)
def write():
    dat= input("Enter the date to remember this note: ")
    with open("journal.txt","a") as file:
        file.write(dat+": ")
    note=input("Enter the note in the journal: ")
    with open ("journal.txt", "a") as file:
        file.write(note + "\n" )


# # write()
# # Read all entries (display them)
def read():
    with open ("journal.txt", "r") as file:
        print(file.read())

# # Search entries by keyword
# def search():
#     with open ("journal.txt", "r") as file:
#         keyword=input("Search note through journal date/word of your choice")
#         for line in file:
#             if keyword in line:
#                 print(line)

# Delete an entry (optional, harder)
# Loop until quit
