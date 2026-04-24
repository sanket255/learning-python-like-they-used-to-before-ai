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

