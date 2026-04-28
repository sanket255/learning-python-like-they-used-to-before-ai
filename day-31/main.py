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
                






