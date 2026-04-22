# User: Sanket
# Tasks: ['A', 'B']

# User: Riti
# Tasks: ['X']

class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []
    def add_task(self, task):
        (self.tasks).append(task)
    def show (self):
        print(f"{self.name}: {self.tasks}")

class TaskManager:
    def __init__(self):
        self.data = {}
    def save_in_dict (self,name,task):
        if self.data[name] in task:
            self.data[name].append(task)
        else:
            self.data[name] = [task]
    def show_dict(self , name , task):
        print(f"{name}: {task}")



while True:
    name = input("Enter name (or quit) : ")
    if name == "quit":
        break
    usr = User(name)
    rt= TaskManager()
    task = input("Enter  task (or quit): ")
    if task == "quit":
        break
    usr.add_task(task)
    usr.show()
    rt.save_in_dict(name , task)    
    rt.show_dict(name , task )










