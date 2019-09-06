"""
学生成绩管理系统
    1.根据姓名查看学生所有成绩
    2.查看所有人的某学科成绩
    3.查看总平均分
    4.查看某人的某学科成绩
    5.根据姓名删除学生信息

增强版要求(选做)
    1.首先编写json格式的数据文件  内容为学生
    2.将json数据解析后转换为学生对象在进行增删改查
"""

# 基本版本
class StudentsScore:

    def __init__(self, student_dict):
        self.student_dict = student_dict

    # 1.根据姓名查看学生所有成绩
    def check_score(self, name):
        # if name in self.student_dict:
        #     return self.student_dict[name]
        # else:
        #     return
        return self.student_dict.get(name)

    # 2.查看所有人的某学科成绩
    def check_all_score(self, subject):
        name_score_dict = {}
        for name, score_dict in self.student_dict.items():
            name_score_dict[name] = score_dict[subject]

        return name_score_dict

    # 3.查看总平均分
    def check_average(self):
        sum_score = 0
        subject_count = 0
        for score_dict in self.student_dict.values():
            for score in score_dict.values():
                sum_score += score
                subject_count += 1
        return sum_score / subject_count

    # 4.查看某人的某学科成绩
    def check_some_score(self, name, subject):
        # return self.student_dict[name][subject]
        student_name = self.student_dict.get(name)
        if student_name:
            return student_name.get(subject)
        else:
            return '没有这个学生'

    # 5.根据姓名删除学生信息
    def drop_student_info(self, name):
        if name in self.student_dict:
            self.student_dict.pop(name)
            return self.student_dict
        else:
            return '没有这个学生'


stu_dict = {
    'Albert1': {'Chinese': 80, 'Math': 100, 'English': 95},
    'Albert2': {'Chinese': 83, 'Math': 90, 'English': 99},
    'Albert3': {'Chinese': 96, 'Math': 79, 'English': 98}
}

# 实例化对象
stu_score = StudentsScore(stu_dict)

# 1.根据姓名查看学生所有成绩
res1 = stu_score.check_score('Albert')
res2 = stu_score.check_score('Albert1')
print(res1)
print(res2)

# 2.查看所有人的某学科成绩
res3 = stu_score.check_all_score('Math')
res4 = stu_score.check_all_score('Chinese')
print(res3)
print(res4)

# 3.查看总平均分
res5 = stu_score.check_average()
print(res5)

# 4.查看某人的某学科成绩
res5 = stu_score.check_some_score('Albert', 'Math')
res6 = stu_score.check_some_score('Albert3', 'Math')
res7 = stu_score.check_some_score('Albert3', 'Chinese')
print(res5)
print(res6)
print(res7)

# 5.根据姓名删除学生信息
res8 = stu_score.drop_student_info('Albert')
res9 = stu_score.drop_student_info('Albert1')
print(res8)
print(res9)



# 增强版本
import json
import os

"""
学生成绩管理系统
    1.根据姓名查看学生所有成绩
    2.查看所有人的某学科成绩
    3.查看总平均分
    4.查看某人的某学科成绩
    5.根据姓名删除学生信息

增强版要求(选做)
    1.首先编写json格式的数据文件  内容为学生
    2.将json数据解析后转换为学生对象在进行增删改查
"""


class StudentsScore:

    def __init__(self, student_dict):
        self.student_dict = student_dict
        for name, score_dict in student_dict.items():
            with open('%s.json' % name, 'w', encoding='utf-8') as f:
                json.dump(score_dict, f)
                f.flush()

    # 1.根据姓名查看学生所有成绩
    def check_score(self, name):
        # # if name in self.student_dict:
        # #     return self.student_dict[name]
        # # else:
        # #     return
        # return self.student_dict.get(name)
        user_path = '%s.json' % name
        if os.path.exists(user_path):
            with open(user_path, 'r', encoding='utf-8') as f:
                user_dic = json.load(f)
                return user_dic
        else:
            return

    # 2.查看所有人的某学科成绩
    def check_all_score(self, subject):
        # name_score_dict = {}
        # for name, score_dict in self.student_dict.items():
        #     name_score_dict[name] = score_dict[subject]
        #
        # return name_score_dict
        name_score_dict = {}
        path_list = os.listdir('/Users/mayite/Desktop/path01')
        for name_path in path_list:
            if name_path.endswith('json'):
                with open(name_path, 'r', encoding='utf-8') as f:
                    student_score_dict = json.load(f)
                    name_score_dict[name_path[:-5]] = student_score_dict[subject]

        return name_score_dict

    # 3.查看总平均分
    def check_average(self):
        # sum_score = 0
        # subject_count = 0
        # for score_dict in self.student_dict.values():
        #     for score in score_dict.values():
        #         sum_score += score
        #         subject_count += 1
        # return sum_score / subject_count
        sum_score = 0
        subject_count = 0
        path_list = os.listdir('/Users/mayite/Desktop/path01')
        for name_path in path_list:
            if name_path.endswith('json'):
                with open(name_path, 'r', encoding='utf-8') as f:
                    student_score_dict = json.load(f)
                    for score in student_score_dict.values():
                        sum_score += score
                        subject_count += 1

        return sum_score / subject_count

    # 4.查看某人的某学科成绩
    def check_some_score(self, name, subject):
        # # return self.student_dict[name][subject]
        # student_name = self.student_dict.get(name)
        # if student_name:
        #     return student_name.get(subject)
        # else:
        #     return '没有这个学生'
        path_list = os.listdir('/Users/mayite/Desktop/path01')
        for name_path in path_list:
            if name_path[:-5] == name:
                with open(name_path, 'r', encoding='utf-8') as f:
                    student_score_dict = json.load(f)
                    return student_score_dict[subject]
        else:
            return '没有这个学生'

    # 5.根据姓名删除学生信息
    def drop_student_info(self, name):
        # if name in self.student_dict:
        #     self.student_dict.pop(name)
        #     return self.student_dict
        # else:
        #     return '没有这个学生'
        path_list = os.listdir('/Users/mayite/Desktop/path01')
        for name_path in path_list:
            if name_path[:-5] == name:
                os.remove(name_path)

                return '删除成功', os.listdir('/Users/mayite/Desktop/path01')
        else:
            return '没有这个学生'


stu_dict = {
    'Albert1': {'Chinese': 80, 'Math': 100, 'English': 95},
    'Albert2': {'Chinese': 83, 'Math': 90, 'English': 99},
    'Albert3': {'Chinese': 96, 'Math': 79, 'English': 98}
}

# 实例化对象
stu_score = StudentsScore(stu_dict)

# 1.根据姓名查看学生所有成绩
res1 = stu_score.check_score('Albert')
res2 = stu_score.check_score('Albert1')
print(res1)
print(res2)

# 2.查看所有人的某学科成绩
res3 = stu_score.check_all_score('Math')
res4 = stu_score.check_all_score('Chinese')
print(res3)
print(res4)

# 3.查看总平均分
res5 = stu_score.check_average()
print(res5)

# 4.查看某人的某学科成绩
res5 = stu_score.check_some_score('Albert', 'Math')
res6 = stu_score.check_some_score('Albert3', 'Math')
res7 = stu_score.check_some_score('Albert3', 'Chinese')
print(res5)
print(res6)
print(res7)

# 5.根据姓名删除学生信息
res8 = stu_score.drop_student_info('Albert')
res9 = stu_score.drop_student_info('Albert1')
print(res8)
print(res9)
    
