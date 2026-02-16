from StudentManagement.Student import Student


class StudentsManager:

    def __init__(self):
        self.students = []


    def create_student(self,name, username, age, courses, gender, state):
        self.students.append(Student(name, username, age, courses, gender, state))

    def update_student_age(self, user_name, new_age):
        for student in self.students:
            if student.username == user_name:
                    student.set_age(new_age)



    def update_student_name(self, username, new_name):
        for student in self.students:
            if student.username == username:
                student.set_name(new_name)




    def update_student_address(self, username, new_gender):
        for student in self.students:
            if student.username == username:
                student.set_gender(new_gender)




    def update_student_state(self,  username, new_state):
        for student in self.students:
            if student.username == username:
                student.set_state(new_state)


    def update_student_course(self,  username, key, old_course, new_course):
        for student in self.students:
            if new_course not in  student:
                student.update(new_course)

        return student_list