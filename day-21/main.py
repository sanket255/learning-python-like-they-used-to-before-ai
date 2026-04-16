# Class:
# NoteBook


class NoteBook:
# Methods:
# add_note(note)
# adds note to memory

    def add_note(self,date,note):
        notes=[]
        self.note=note
        notes.append(self.note)
# saves to file
        with open ("notebook.txt", "a") as file:
            file.write((f"{date}: {self.note}") + "\n")

# show_notes()
    def show_notes(self):
        with open ("notebook.txt", "r") as file:
            print(file.read())


notebook= NoteBook()
ask="0"
while ask!='quit':
    notebook.add_note(input("Enter the date today: "),input("Enter the note Today that Tomorrow you will read: "))
# prints all notes from file
    notebook.show_notes()
    ask=input("another note? ( y/quit ):")


