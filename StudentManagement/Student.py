class Student:

    def __init__(self, name, username, age, courses, gender, state):
        self.__name = name
        self.__username = username
        self.__age = age
        self.__courses = courses
        self.__gender = gender
        self.__state = state


    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name



    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username




    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age




    def set_courses(self, courses):
        self.__courses = courses

    def get_courses(self):
        return self.__courses




    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender




    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state


