import random

class Student:
    def __init__(self, name, year, program, acronym):
        self.name = name
        self.year = year
        self.program = program
        self.acronym = acronym
        self.grade = None


    def rendom_grade(self):
        self.grade = random.choice(["A", "B", "C", "D", "E", "F"])

    


student1 = Student("Hassan", 2025, "El och energi", "hasa9288")

print(student1.program)
student1.program = "teknik"
print(student1.program)


print(student1.grade)
student1.rendom_grade()
print(student1.grade)