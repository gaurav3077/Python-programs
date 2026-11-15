class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def show_details(self):
        print("Student name:", self.name)
        print("Course:", self.course)


student = Student(input("Enter student name: "), input("Enter course: "))
student.show_details()
