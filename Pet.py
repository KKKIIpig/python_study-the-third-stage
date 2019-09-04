"""
利用多态与封装设计一个虚拟宠物的程序
要求：
1.创建三个宠物主人，分别养的是不同的三种宠物
2.三个主人进行喂食的时候，对应的宠物就会完成进食
"""
import abc
class Pet(metaclass=abc.ABCMeta):
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,x):
        self.__name = x
    @abc.abstractmethod
    def eat(self):
        pass

class Cat(Pet):
    def __init__(self,name,type):
        self.__type = type
        super().__init__(name)
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,x):
        self.__type = x
    def eat(self):
        print('吃猫粮')

class Dog(Pet):
    def __init__(self,name,type):
        self.__type = type
        super().__init__(name)
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,x):
        self.__type = x
    def eat(self):
        print('吃狗粮')

class Pig(Pet):
    def __init__(self,name,type):
        self.__type = type
        super().__init__(name)
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,x):
        self.__type = x
    def eat(self):
        print('吃猪粮')

class Master:
    def __init__(self,name,pet):
        self.__name = name
        self.__pet = pet
    def feed(self):
        print('%s主人准备好宠物粮食' %self.__name)
        print('%s品种的%s宠物来进食' %(self.__pet.type,self.__pet.name))
        self.__pet.eat()

pet1 = Cat('June','蓝猫')
pet2 = Dog('July','柴犬')
pet3 = Pig('October','香猪')
master1 = Master('kiki',pet1)
master2 = Master('mo',pet2)
master3 = Master('albert',pet3)

master1.feed()
