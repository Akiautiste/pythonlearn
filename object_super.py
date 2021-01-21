# coding:utf-8

class Parent(object):
    def __init__(self, p):
        print(f'i am parent:{p}')


class Child(Parent):
    def __init__(self, c, p):
        print(f'i am child:{c}')
        super().__init__(p)


if __name__ == '__main__':
    c = Child(p='Pa', c='Ch')
