"""
使用组合与继承设计一个学生选择课程的程序，
使老师和学生初始化都具有课程属性，但是属性值为空，可以动态添加，
可打印出老师教授的的课程和学生学习的课程，
可以打印出课程名字和价格，
尽量避免写重复代码（提示：学生和老师都是属于人，都有课程属性）
"""


class DeepsharePeople:
    school = 'deepshare'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class DeepshareTeacher(DeepsharePeople):
    def __init__(self, name, age, sex, level, salary):
        super().__init__(name, age, sex)
        self.level = level
        self.salary = salary

        self.courses = []

    def change_score(self):
        print('teacher %s is changing score' % self.name)

    def tell_course_info(self):
        print(('老师%s 教授的课程信息如下' % self.name).center(50, '='))
        for course_obj in self.courses:
            course_obj.info()


class DeepshareStudent(DeepsharePeople):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex, )
        self.courses = []

    def choose(self):
        print('student %s choose course' % self.name)

    def tell_course_info(self):
        print(('学生%s 学习的课程信息如下' % self.name).center(50, '='))
        for course_obj in self.courses:
            course_obj.info()


class Course:
    def __init__(self, cname, period, price):
        self.cname = cname
        self.period = period
        self.price = price

    def info(self):
        print('课程信息<名字：%s 周期：%s  价钱：%s>' % (self.cname, self.period, self.price))


tea1 = DeepshareTeacher('Albert', 18, 'male', 9, 3.1)
stu1 = DeepshareStudent('张三', 16, 'male')

python = Course('Python', '2mons', 1000)
database = Course('database', '3mons', 2000)
AI = Course('AI', '8mons', 3000)

# 给老师添加课程
tea1.courses.append(python)
tea1.courses.append(database)

tea1.courses[0].info()
for course_obj in tea1.courses:
    course_obj.info()

tea1.tell_course_info()

# 给学生添加课程
stu1.courses.append(python)
stu1.courses.append(AI)
stu1.courses.append(database)
stu1.tell_course_info()
