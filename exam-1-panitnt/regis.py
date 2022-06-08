from student import Student
from course import Course


class Regis:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.enroll_std = {}
        self.enroll_courses = {}

    def add_student(self, std_class):
        self.students[std_class.id] = std_class
        self.enroll_std[std_class.id] = []

    def add_course(self, regis_class):
        self.courses[regis_class.id] = regis_class
        self.enroll_courses[regis_class.id] = []

    def enroll(self, std_id, regis_id):
        enroll_sub = self.enroll_std[std_id]
        regis_sub = self.courses[regis_id]
        enroll_sub.append(regis_sub)
        enroll_course = self.enroll_courses[regis_sub.id]
        enroll_course.append(self.students[std_id])

    def enrollments_by_student_id(self, std_id):
        courses_regis = self.enroll_std[std_id]
        return courses_regis

    def enrollments_by_course_id(self, course_id):
        course_regis_by_id = self.enroll_courses[course_id]
        return course_regis_by_id


if __name__ == '__main__':
    import doctest
    doctest.testfile('docs/regis.md')
