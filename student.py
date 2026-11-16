"""
    该文件用于记录学生信息(姓名， 性别， 年龄， 手机号， 详细信息)

"""

class Student:
    def __init__(self, name, grade, age, number, infor):
        self.name = name
        self.grade = grade
        self.age = age
        self.number = number
        self.infor = infor

    def __str__(self):
        return f'学生姓名:{self.name}, 学生性别:{self.grade}, 学生年龄:{self.age}, 学生联系方式:{self.number}, 学生详细信息:{self.infor}'
