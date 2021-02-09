# coding:utf-8
import os


def create_package(path):
    if os.path.exists(path):
        raise Exception(f'{path}已经存在不可创建')
    os.makedirs(path)
    init_path = os.path.join(path, '__init__.py')
    f = open(init_path, 'w')
    f.write("'coding:utf-8'\n")
    f.close()


class Open(object):
    def __init__(self, path, mode='w', isreturn=True):
        self.path = path
        self.mode = mode
        self.isreturn = isreturn

    def write(self, message):
        f = open(self.path, mode=self.mode,encoding='utf-8')
        if self.isreturn:
            message = '%s\n' % message
        f.write(message)
        f.close()

    def read(self, is_strip=True):
        result = []
        with open(self.path, mode=self.mode, encoding='utf-8') as f:
            data = f.readlines()
        for line in data:
            if is_strip:
                temp =line.strip()
                if temp != '':
                    result.append(temp)
            else:
                if line != '':
                    result.append(line)
        return result

if __name__ == '__main__':
    current_path = os.getcwd()
    # path = os.path.join(current_path,'test1')
    # create_package(path)
    open_path = os.path.join(current_path, 'package_datetime.py')
    # o = Open(open_path)
    # o.write('hello python')
    o = Open(open_path, mode='r')
    # o.read()
    data = o.read()
    print(data)