# print("task manager!!")

class TaskManager:
    def __init__(self):
        print("task manager")
        self.data={}


    def add_task(self, category, task):
        self.category=category
        self.task=task
        if category in self.data:
            self.data[category].append(task)
        else:
            self.data[category] = [task]