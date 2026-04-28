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
                elif keyword not in lines:
                    return "result not found!!!"

        return all_lines
                






fr = FileReader()

print("INSTRUCTIONS!!")
print("1. dont add '.txt' suffix we have that in our programme.")
print("2. once you choose file at beginning thats the file \n youre doing operations on until \n you quit and start over with different file.")
print("3. we suggest to look our file database before choosing \n file that way you dont mess up \n the name up your file")
print("4. while searching by keyword we suggest to enter the \n keyword in all lower case so you dont miss any content \n  at all from the file it self")




while True:
    
    filename = input("Enter the filename(Enter name of the file to read)/\n look in our file database (lookin) /\n (or quit ): ")
    
    if filename == "quit":
        break
    ask = input("Do you want to look our file's database (y/n): ")
    if filename == "lookin" or ask == "y":
        result = fr.show_list()
        for i, result in enumerate(result):
            print(f"{i}: {result}")




    ask = input("do you want to search through file? ( y / quit ): ")
    if ask == "y":
        keyword = input("search by keyword: ")
        search = fr.search( filename, keyword )
        print(search)

    
    elif ask == "quit":
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
        
        

        


# List: Use os.listdir() to show the user what is there.
# Filter: Use os.path.isfile() to ensure they only see files, not folders.
# Search: If they type a name, use os.path.exists() to verify it before trying to open it.