"""
    该文件用于操作学生系统, 实现对学生信息的增, 删, 改, 查, 保存, 退出功能

"""
from student import Student

class StudentCMS:
    def __init__(self):
        self.stu_list = []

    def show(self):
        print("*" * 30)
        print("欢迎使用教务系统1.0版本")
        print("1.添加学生信息")
        print("2.删除学生信息")
        print("3.更改学生信息")
        print("4.查找单个学生信息")
        print("5.查找所有学生信息")
        print("6.保存学生信息")
        print("7.退出系统")
        print("*" * 30)

    # 添加学生信息
    def add_student(self):
        name = input("请输入学生姓名:")
        grade = input("请输入学生性别:")
        age = input("请输入学生年龄:")
        number = input("请输入学生联系方式:")
        infor = input("请输入学生详细信息(比如:兴趣爱好, 学生性格等):")
        student = Student(name, grade, age, number, infor)
        self.stu_list.append(student)
        print(f"添加{name}学生信息成功\n")

    # 删除学生信息
    def del_student(self):
        if len(self.stu_list) == 0:
            print("暂无学生信息")
        else:
            del_student = input("请输入删除学生的姓名:")
            for stu in self.stu_list:
                if stu.name == del_student:
                    self.stu_list.remove(stu)
        print(f"删除{del_student}学生信息成功\n")

    # 更改学生信息
    def update_student(self):
        if len(self.stu_list) == 0:
            print("暂无学生信息")
        else:
            update_student = input("请输入更改学生的姓名:")
            for stu in self.stu_list:
                if stu.name ==  update_student:
                    update_name = input("更改后的学生姓名:")
                    update_grade = input("更改后的学生性别:")
                    update_age = input("更改后的学生年龄:")
                    update_number = input("更改后的学生联系方式:")
                    update_infor = input("更改后的学生详细信息:")

                    stu.name = update_name
                    stu.grade = update_grade
                    stu.age = update_age
                    stu.number = update_number
                    stu.infor = update_infor
                    break
                else:
                    print("该学生不存在")
        print(f"更改{update_student}学生信息成功\n")

    # 查找单个学生信息
    def show_one_student(self):
        if len(self.stu_list) == 0:
            print("暂无学生信息")
        else:
            show_one_student = input("请输入查找学生的姓名:")
            for stu in self.stu_list:
                if stu.name == show_one_student:
                    print(stu)
        print(f"查找{show_one_student}学生信息成功\n")

    # 查找全部学生信息
    def show_all_student(self):
        if len(self.stu_list) == 0:
            print("暂无学生信息")
        else:
            for stu in self.stu_list:
                print(stu)
        print("以上是全部学生信息\n")

    # 保存学生信息
    def save_student_infor(self):
        with open("./students_data.txt", "w", encoding="utf-8") as student_save:
            stu_dict = [sut.__dict__ for sut in self.stu_list]
            student_save.write(str(stu_dict))

    # 加载学生信息
    def load_student_infor(self):
        try:
            with open("./students_data.txt", "r", encoding="utf-8") as student_load:
                stu_data = student_load.read() # "[ {} ]"
                stu_list = eval(stu_data)
                if len(stu_list) == 0:
                    stu_list = []

                self.stu_list = [Student(**stu) for stu in stu_list]
        except:
            with open("./students_data.txt", "w", encoding="utf-8") as student_load:
                pass

    # 运行程序函数
    def main(self):
        self.load_student_infor()
        while True:
            self.show()
            print()
            user_input = input("请输入数字编号选择你想要执行的操作 -->")
            if user_input == "1":
                self.add_student()
            elif user_input == "2":
                self.del_student()
            elif user_input == "3":
                self.update_student()
            elif user_input == "4":
                self.show_one_student()
            elif user_input == "5":
                self.show_all_student()
            elif user_input == "6":
                self.save_student_infor()
                print("保存学生信息成功")
            elif user_input == "7":
                exit_input = input("是否确定退出系统 (Y 退出/N 取消退出) -->")
                if exit_input.lower() == "y":
                    self.save_student_infor()
                    print("欢迎使用教务系统")
                    break
                print()