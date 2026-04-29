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
                result = self.search_infile(f,keyword)
                final_result[f] = result
    
        return final_result












