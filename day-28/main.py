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

    def del_name (self, name , contact):
        if name in self.data:
            print(self.data[name])
            if contact in self.data[name]:
                self.data[name].remove(contact)
                if len(self.data[name]) == 0:
                    del self.data[name]
                    print(self.data)
                else:
                    print("it does not exist!!")
            else:
                print(f"{contact} doesn't exist in  {name}!!")
        else:
            print(f"{name} not found!!")
        

        

        
        


cc = ContactBook()
while True:
    name = input("Enter name: ")
    contact = input("Enter contact number: ")
    
    result = cc.add_name(name, contact)
    
    search = input("enter the name of the contact you want number for (or quit): ")
    
    if search != "quit":
        result = cc.get_data(search)
    elif search == "quit":
        break

    all = input("do you want to see whole contact list? (y/quit) : ")
    
    if all != "quit":
        result = cc.show_all()
    elif all == "quit":
        break

    delete = input("enter the name you want to delete (or quit) : ")
    if delete == "quit":
        break
    delete_num = input("Enter the number: ")
    result = cc.del_name(delete,delete_num)

    print(result)
    
    # elif delete!="quit":