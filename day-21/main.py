import json

# Class:
# NoteBook


class NoteBook:
# Methods:
# add_note(note)
# adds note to memory

    def add_note(self,date,note):
        try:
            with open ("notebook.json","r") as file:
                data=json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        
        if date in data:
            data[date].append(note)
        else:
            data[date] = [note]

        with open ("notebook.json" , "w") as file:
            json.dump(data,file, indent =4)
            
#         notes = {}
#         all_notes = []
#         self.note=note
#         notes.(self.note)
# # saves to file
#         with open ("notebook.json", "w") as file:
#             json.dump((f"{date}: {self.note}") + "\n")

# show_notes()
    def show_notes(self):
        try:
            with open ("notebook.json", "r") as file:
                data=(json.load(file))
            for date in data:
                print("hi")

        except FileNotFoundError:
            print("File doesnt exist!!!")



# notebook= NoteBook()
# ask="0"
# while ask!='quit':
#     notebook.add_note(input("Enter the date today: "),input("Enter the note Today that Tomorrow you will read: "))
# # prints all notes from file
#     notebook.show_notes()
#     ask=input("another note? ( y/quit ):")


