import os

class FileSearch:
    def get_list(self):
        folder = "/home/scar/learnpy/day-32"
        return os.listdir(folder)

    def search_infile(self,filename,keyword):
        match= []
        with open (f"{filename}", "r") as file:
            for lines in file:
                
                if keyword.lower() in lines.lower():
                    match.append(lines.strip())

            return match
    
    def search_infolder(self,keyword):
        final_result = {}
    
        folder = "/home/scar/learnpy/day-32"
        files = os.listdir(folder)
    
        for f in files:
            if f.endswith(".txt"):
                full_path = os.path.join(folder,f)
                result = self.search_infile(full_path,keyword)
                final_result[f] = result
    
        return final_result

fs = FileSearch()

print("INSTRUCTIONS!!\n\n" )
print("1. Enter the file extention when entering the file name \n\n example(file.txt)\n\n\n")


while True:
    show = fs.get_list()
    print(show)

    ask = input("do you want to search through a perticuler file(a) \n\nor in everyfile in the folder(b) or (quit): ")
    if ask == "quit":
        break
    if ask == "a":
        filename = input("name the file you want to search through: ")
        keyword = input("Enter the word that you want to search  through: ")
        result = fs.search_infile(filename, keyword)
        print (result)
    if ask == "b":
        keyword = input("Enter the word that you want to search  through: ")
        result = fs.search_infolder(keyword)
        print (result)













