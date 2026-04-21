class StudentGradeSys:
    def __init__(self):
        self.data = {}
    def add_grade(self, student, grade):
        if student in self.data:
            self.data[student].append(grade)
        else:
            self.data[student] = [grade]

    def show_students(self,student):
        if student in self.data:
            print(self.data[student])
        
    def avg(self, student):
        a = self.data[student]
        b = sum(a)
        c= b / len(a)
        print(c)







