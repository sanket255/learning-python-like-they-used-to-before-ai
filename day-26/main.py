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
        if name in self.data:
            self.data[name].add_task(task)
        else:
            existing_people = User(name)
            existing_people.add_task(task)
            self.data[name] = existing_people

    def show_dict(self,name,task):
        print(f"{name}: {task}")
        print(self.data)


rt= TaskManager()
while True:
    name = input("Enter name (or quit) : ")
    if name == "quit":
        break
    # usr = User(name)
    task = input("Enter  task (or quit): ")
    if task == "quit":
        break
    rt.save_in_dict(name , task)    
    rt.show_dict(name , task)










