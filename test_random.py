# coding:utf-8

import random

gitfs = ['iphone','ipad','appleWatch','macbook']

def choice_gitfs():
    gift = random.choice(gitfs)
    print(f'你得到了{gift}')

def choice_gitf_new():
    count = random.randrange(0,100,1)
    if 0 <=count <= 50:
        print('你中了一个iphone')
    elif 50 < count <= 70:
        print('你中了一个ipad')
    elif 70 < count < 90:
        print('你中了一个applewatch')
    else:
        print('你中了一个macbook')
    print(count)
if __name__ == '__main__':
    choice_gitf_new()