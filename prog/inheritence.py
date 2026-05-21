class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def age_up(self):
        self.age += 1

class Student(Person):
    def __init__(self, name, age, height, year, grade):
        super().__init__(name, age, height)
        self.year = year
        self.grade = grade

class Teacher(Person):
    def __init__(self, name, age, height, subject, coffee_cup_count):
        super().__init__(name, age, height)
        self.subject = subject 
        self.coffee_cup_count = coffee_cup_count
    
teacher1 = Teacher("Mattias Leijon", 54, 140, "El", 690)
student1 = Student("Osama Bin Ladin", 13, 190, 7, "F-")

print(teacher1.age)
teacher1.age_up
print(teacher1.age)

class Animal:
    def __init__(self, name, age, leg_count):
        self.name = name
        self.age = age
        self.leg_count = leg_count

class Dog(Animal):
    def __init__(self, name, age, leg_count, race, hair_amount):
        super().__init__(name, age, leg_count)
        self.race = race 
        self.hair_amount = hair_amount

class Chicken(Animal):
    def __init__(self, name, age, leg_count, egg_count):
        super().__init__(name, age, leg_count)
        self.egg_count = egg_count
        