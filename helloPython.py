class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} + {self.age}"


class Student(Person):
    def __init__(self, classroom):
        super().__init__("Dat", 13)
        self.classroom = classroom

    def __iter__(self):
        self.value = 1
        return self

    def __next__(self):
        x = self.value
        self.value += 1
        return x
    def wellcome(self):
        print(f"{self.name}, {self.age} in class {self.classroom}")
def helloPython():
    global giatri
    giatri = "a"
    return "asdfasdf"
x = helloPython()
print(giatri)
print(x)
student = Student(1)
myiter = iter(student)
print(next(myiter))
student.wellcome()
a = list({1, 2, 3})
