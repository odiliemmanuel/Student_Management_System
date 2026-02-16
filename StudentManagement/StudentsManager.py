from StudentManagement.Student import Student


class Students:

    def __init__(self):
        self.students = []


    def create_student(self,name, username, age, courses, gender, state):
        self.students.append(Student(name, username, age, courses, gender, state))

    def update_student_age(self, student_list, username, key, old_age, new_age):
        for student in student_list[username].get(key):
            if new_age != old_age:
                student.update(new_age)

        return student_list


    def update_student_name(self, student_list, username, key, old_name, new_name):
        for student in student_list[username].get(key):
            if new_name != old_name:
                student.update(new_name)

        return student_list

    def update_student_address(self, student_list, username, key, old_address, new_address):
        for student in student_list[username].get(key):
            if new_address != old_address:
                student.update(new_address)

        return student_list


    def update_student_state(self, student_list, username, key, old_state, new_state):
        for student in student_list[username].get(key):
            if new_state != old_state:
                student.update(new_state)

        return student_list

    def update_student_course(self, student_list, username, key, old_course, new_course):
        for student in student_list[username].get(key):
            if new_course not in  student:
                student.update(new_course)

        return student_list