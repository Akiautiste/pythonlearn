# coding:utf-8

import json
import pickle

def read(path):
    with open(path,'r') as f:
        data = f.read()
    return json.loads(data)

def write(path,data):
    with open(path,'w') as f:
        if isinstance(data,dict):
            _data = json.dumps(data)
            f.write(_data)
        else:
            raise TypeError('data should be a dict')
    return True

data = {'name':'xiaomu','age':18,'top':176}


if __name__ == '__main__':
    write('test.json',data)
    result = read('test.json')
    print(result)