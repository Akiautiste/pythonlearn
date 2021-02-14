# coding:utf-8

import hashlib
import time

base_sign = 'muke'


def custom():
    a_timestamp = int(time.time())
    print(a_timestamp)
    _token = '%s%s' % (base_sign, a_timestamp)
    hashobj = hashlib.sha1(_token.encode('utf-8'))
    a_token = hashobj.hexdigest()
    return a_token, a_timestamp


def b_service_check(token, timestamp):
    _token = '%s%s' % (base_sign, timestamp)
    print(timestamp)
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest()
    if token == b_token:
        return True
    else:
        return False


if __name__ == '__main__':
    need_help_token, timestamp = custom()
    result = b_service_check(need_help_token, int(time.time()))
    if result:
        print('A合法')
    else:
        print('B不合法')
