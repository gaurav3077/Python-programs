class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_course(self):
        print("I am studying", self.course)


student = Student(input("Enter your name: "), input("Enter your course: "))
student.introduce()
student.show_course()
