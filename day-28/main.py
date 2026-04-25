class ContactBook:
    def __init__(self):
        self.data = {}
        
    def add_name(self,name,contact):
        if name in self.data:
            self.data[name].append(contact)
        else:
            self.data[name] = contact
        # return self.data
    def get_data(self,name):
        if name in self.data:
            return self.data[name]

    def show_all (self):
        return self.data

    def del_name (self, key , value):
        if key in self.data:
            print(self.data[key])
            if value in self.data[key]:
                self.data[key].remove(value)
                if len(self.data[key]) == 0:
                    del self.data[key]
                    print(self.data)
                else:
                    print("it does not exist!!")
            else:
                print(f"{value} doesn't exist in  {key}!!")
        else:
            print(f"{key} not found!!")
        

        

        
        


