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
        cat=input("Enter the category: ")
        if cat in self.data:
            print(self.data[cat])

    def show_all(self):
        print(self.data)


    def del_task(self):
        key=input("Enter the category to delete from: ")
        if key in self.data:
            print(self.data[key])


            value=input("enter the task you want to delete: ")
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





tm = TaskManager()
while True:
    category=input("Enter catagory(study(s) / work(w) / random(r) /quit ): ")
    if category=="quit":
        break
    task=input("Add task: ")
    tm.add_task(category,task)
    view=input("Do you want to check the list (y/n): ")
    if view=="y":
        tm.view_task()
    show=input("want to check all the tasks(y/n): ")
    if show == "y":
        tm.show_all()
    dele=input("do you want to delete something (y/n): ")
    if dele=="y":
        tm.del_task()
