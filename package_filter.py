# coding:utf-8

from functools import reduce

fruits = ['apple', 'banana', 'orange']

result = filter(lambda x: 'e' in x, fruits)
print(list(result))
print(fruits)


def filter_func(item):
    if 'e' in item:
        return True


print('--------')
filter_result = filter(filter_func, fruits)
print(list(filter_result))

map_result = map(filter_func, fruits)
print(list(map_result))

reduce_result = reduce(lambda x,y:x*y, [2,3,2,5])
print(reduce_result)

reduce_result_str = reduce(lambda x,y:x+y, fruits)
print(reduce_result_str)