#coding:utf-8

def test(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))

test(1,2,3,4,5,name='hello')

