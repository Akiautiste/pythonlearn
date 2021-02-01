# coding:utf-8

def test2():
    try:
        1/0
    except Exception as e:
        return e
    finally:
        print('finally')

result = test2()
print(result)