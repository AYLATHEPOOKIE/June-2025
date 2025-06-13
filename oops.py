class student():
    def __init__(self,name,age,grade,teacher,house):
        self.name=name
        self.age=age
        self.grade=grade
        self.teacher=teacher
        self.house=house
        self.school="THE SCHOOL"

    def display(self):
        print(f"{self.name},{self.age},{self.grade},{self.teacher},{self.house},{self.school}")


stu1=student("Jimmy","12","7","Ms hjeiop","House cjfp")
stu1.display()
print(stu1.teacher)