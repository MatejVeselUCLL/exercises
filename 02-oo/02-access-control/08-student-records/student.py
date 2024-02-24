class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    # Q& Could this be a static method, because it does not depend on any of the instance fields?
    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif score in range(80, 89+1):
            return "B"
        elif score in range(70, 79+1):
            return "C"
        elif score in range(60, 69+1):
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        self.__courses[course_name] = self.calculate_letter_grade(score)

    def get_courses(self):
        return self.__courses