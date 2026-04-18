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

    def view_task(self):
        # data={}
        cat=input("Enter the category: ")
        if cat in self.data:
            print(self.data[cat])

    def show_all(self):
        print(self.data)


    def del_task(self):
        key=input("Enter the catogory: ")
        if key in self.data:
            value=input("enter the task you want to delete: ")
            if value in self.data[key]:
                self.data[key].remove(value)

        if len(self.data[key]) == 0:
            # self.data
            del self.data[key]
            print(self.data)