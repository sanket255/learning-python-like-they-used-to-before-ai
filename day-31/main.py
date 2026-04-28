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

        
