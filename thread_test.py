# coding:utf-8

import random
import time

list = ['python','django','tornado','flask','bs5','requests','uvloop']

new_lists = []

def work():
    if len(list) == 0:
        return
    data = random.choice(list)
    list.remove(data)
    new_data = '%s_new' % data
    new_lists.append(new_data)

if __name__ == '__main__':
    start = time.time()
    for i in range(len(list)):
        work()
    print('old list:',list)
    print('new list:',new_lists)
    print('time is %s' % (time.time() - start))
