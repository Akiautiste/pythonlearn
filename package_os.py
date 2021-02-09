# coding:utf-8

import os

current_path = os.getcwd()
print(current_path)

new_path = f'{current_path}/test1'
try:
    os.makedirs(new_path)
except Exception as e:
    print(e)

data = os.listdir(current_path)
print(data)

os.removedirs('test1')