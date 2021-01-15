# coding:utf-8

if __name__ == '__main__':
    info = 'python is a glamour language'
    result = 'glamour' in info
    print(result)

    result = 'language' not in info
    print(result)

    info2 = 'python is a great code'
    print(max(info2))
    print('.',min(info2),'.')

    info3 = 'excercise is good'
    info4 = ' traning'
    new_str = info3+info4
    print(new_str)
    print(len(new_str))
    length = len(new_str)
    print(type(length))

