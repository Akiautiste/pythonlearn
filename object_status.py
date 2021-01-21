# coding:utf-8

# 1 定义一个父类
class Parent(object):
    def talk(self):
        print('Parent are Talking !!!')


# 2 定义一个子类，继承父类
class Brother(Parent):
    def run(self):
        print('Brother is running !!!')

    def talk(self):
        print('Brother is talking !!!')

class Sister(Parent):
    def talk(self):
        print('Sister is talkking !!!')

if __name__ == '__main__':
    a_brother = Brother()
    a_brother.run()
    a_brother.talk()
    parent = Parent()
    parent.talk()
    sister = Sister()
    sister.talk()

# 为什么要使用多态
# 为什么要继承父类
# 答：为了使用已经写好的类的函数
# 答：为了保留子类中某个和父类中名称一样的函数的功能，可以保留子类中的函数功能