"""
学生成绩管理系统
    1.根据姓名查看学生所有成绩
    2.查看所有人的某学科成绩
    3.查看总平均分
    4.查看某人的某学科成绩
    5.根据姓名删除学生信息

增强版要求:
    1.首先编写json格式的数据文件，内容为学生
    2.将json数据解析后转换为学生对象再进行增删改查
"""

stu_dic = {
    'kiki':{'Chinese':90,'Math':98,'English':100},
    'mo':{'Chinese':99,'Math':95,'English':96},
}

class NameAllGrade:
    def __init__(self,name):
        self.name = name
    def look(self):
        for v in stu_dic[self.name]:
            print('%s的成绩为:%s' %(self.name,stu_dic[self.name][v]))

class WhichAllGrade:
    def __init__(self,subject):
        self.subject = subject
    def look(self):
        for k,i in stu_dic.items():
            print('%s的%s成绩为:%s' %(k,self.subject,i[self.subject]))

class TotalScore:
    def __init__(self,subject):
        self.subject = subject
    def sum(self):
        n = 0
        sum = 0
        for i in stu_dic.values():
            sum += i[self.subject]
            n += 1
        total_score = sum/float(n)
        print('%s的总平均分为:%s' %(self.subject,total_score))

class AnybodyAnygrade:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
    def look(self):
        grade = stu_dic[self.name][self.subject]
        print('%s的%s成绩为:%s' %(self.name,self.subject,grade))

class DeleteData:
    def __init__(self,name):
        self.name = name
    def delete(self):
        del stu_dic[self.name]


print("""
--------学生成绩管理系统--------
    1.根据姓名查看学生所有成绩
    2.查看所有人的某学科成绩
    3.查看总平均分
    4.查看某人的某学科成绩
    5.根据姓名删除学生信息
""")
while True:
    choice = input('请输入选项(输入q退出系统)>>:')
    if choice == '1':
        n = input('请输入该学生姓名>>:')
        NameAllGrade(n).look()
    if choice == '2':
        s = input('请输入该学科名>>:')
        WhichAllGrade(s).look()
    if choice == '3':
        s = input('请输入该学科名>>:')
        TotalScore(s).sum()
    if choice == '4':
        n = input('请输入该学生姓名>>:')
        s = input('请输入该学科名>>:')
        AnybodyAnygrade(n,s).look()
    if choice == '5':
        n = input('请输入该学生姓名>>:')
        DeleteData(n).delete()
    if choice == 'q':
        break
