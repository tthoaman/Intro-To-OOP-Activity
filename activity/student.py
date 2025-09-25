class Student:
    def __init__(self, name, year, courses):
        self.name = name
        self.year = year
        self.courses = courses
    
    def add_class(self, course):
        self.courses.append(course)

    def get_num_classes(self):
        return len(self.courses)

    
    def summary(self):
        print(f"{self.name} is a {self.year} enrolled in {self.get_num_classes()} classes")


