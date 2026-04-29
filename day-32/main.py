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
    












