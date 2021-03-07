# coding:utf-8

import time
import os
import multiprocessing

def work_a():
    for i in range(10):
        print(i,'a',os.getpid())
        time.sleep(1)

def work_b():
    for i in range(10):
        print(i,'b',os.getpid())
        time.sleep(1)


if __name__ == '__main__':
    start = time.time() #主进程
    a_p = multiprocessing.Process(target=work_a)
    # a_p.start() #子进程1
    # a_p.join()

    b_p = multiprocessing.Process(target=work_b)
    # b_p.start()#子进程2

    for p in (a_p,b_p):
        p.start()

    for p in (a_p,b_p):
        p.join()

    for p in (a_p,b_p):
        print(p.is_alive())


    print(time.time()-start)
    print('parent pid is %s' % os.getpid())