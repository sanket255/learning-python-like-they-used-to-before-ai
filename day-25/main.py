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
            print(self.data)
        
    def avg(self, student):
        student


sgs = StudentGradeSys()
a = "sanket"
b = 90

sgs.add_grade(a,b)
sgs.show_students(a,b)
