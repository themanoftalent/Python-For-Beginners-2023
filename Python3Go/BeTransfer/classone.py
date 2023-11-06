class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name

        if self.name != " ":
            Student.count += 1
        else:
            Student.count = Student.count #indent
