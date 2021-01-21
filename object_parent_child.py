# coding:utf-8

class Parent(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def talk(self):
        return f'{self.name} are walking'

    def is_sex(self):
        if self.sex == 'boy':
            return f'{self.name} is a boy'
        else:
            return f'{self.name} is a girl'

class ChildOne(Parent):
    def play_football(self):
        return f'{self.name} are playing football'

class ChildTwo(Parent):
    def play_pingpong(self):
        return f'{self.name} are playing pingpong'

if __name__ == '__main__':

    c_one = ChildOne(name=122, sex='boy')
    result = c_one.talk()
    print(result)

    c_two = ChildTwo(name=11, sex=90)
    result = c_two.play_pingpong()
    print(result)


