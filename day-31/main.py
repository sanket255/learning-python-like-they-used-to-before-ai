# 
import os


print ("file system")

class FileReader:
    def read_files(self, filename):
        with open (f"{filename}.txt", "r") as file:
            return (file.read())
   
    def show_list(self):
        folder = "/home/scar/learnpy/day-31"
        return os.listdir(folder)

        
    def search(self,filename, keyword):
        with open (f"{filename}.txt", "r") as file:
            all_lines = []
            for lines in file:
                if keyword in lines.lower() :
                    all_lines.append(lines.strip())

        return all_lines
                






fr = FileReader()

while True:
    
    filename = input("Enter the filename(Enter name of the file to read)  / (or quit ): ")
    
    if filename == "quit":
        break
    
    else:
        while True:
                try:
                    file = fr.read_files(filename)
                    print(file)
                    break
                except FileNotFoundError:
                    print("this file does not exist in our database!")
                    continue
    


    ask = input("look into the files we have? ( y / quit ): ")
    if ask == "y":
        result = fr.show_list()
        for i, result in enumerate(result):
            print(f"{i}: {result - 1}")

    ask = input("do you want to search through file? ( y / quit ): ")
    if ask == "y":
        keyword = input("search by keyword: ")
        search = fr.search( filename, keyword )
        print(search)
    
    elif ask == "quit":
        break

        


# List: Use os.listdir() to show the user what is there.
# Filter: Use os.path.isfile() to ensure they only see files, not folders.
# Search: If they type a name, use os.path.exists() to verify it before trying to open it.