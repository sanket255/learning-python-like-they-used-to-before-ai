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

    def top (self, student):
        best_student = ""
        best_avg = 0
        # top_student_list =dict(best_student , best_avg)
        for student in self.data:    
            stud = self.data[student]
            stud_sum = sum(stud)
            stud_avg= stud_sum / len(stud)
            print(stud_avg)
            if stud_avg > best_avg:
                best_avg = stud_avg
                best_student = student
        
        print (f"{best_student}: {best_avg} ")
        print(self.data)
        
            


sgs = StudentGradeSys()
while True:
    a = input("Enter the student name (or quit): ")
    if a == "quit":
        break
    while True:
        try:
            b = int(input("Enter the marks: "))
            break
        except TypeError:
            print ("try a number")
            continue

while True:
    ask = input  
    sgs.add_grade(a,b)
    sgs.show_students(a)
    sgs.avg(a)
    sgs.top(a)





