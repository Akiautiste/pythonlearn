# coding:utf-8

def out(func):
    def inner(*args,**kwargs):
        result = func(*args,**kwargs)
        if  result == 'ok':
            return 'That\'s ok'
        else:
            return 'That\'s failed'
    return inner
@out
def a(name):
    return  name


print(a('ok'))