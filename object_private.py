# coding:utf-8

class Cat(object):
    __cat_type = 'cat'

    def __init__(self,name,sex):
        self.name = name
        self.__sex = sex
    def run(self):
        result = self.__run()
        print(result)

    def __run(self):
        return f'{self.__cat_type}小猫{self.name}{self.__sex}开心的奔跑着'

    def jump(self):
        result = self.__jump()
        print(result)

    def __jump(self):
        return f'{self.__cat_type}小猫{self.name}{self.__sex}开心的跳着'

cat =Cat(name='mocha',sex='boy')
cat.run()
cat.jump()

print(dir(cat))

print(cat.__sex)