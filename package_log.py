# coding:utf-8

import logging
import os

def init_log(path):
    if os.path.exists(path):
        mode = 'a'
    else:
        mode = 'w'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',
        filename=path,
        filemode=mode
    )
    return logging

current_path = os.getcwd()
path = os.path.join(current_path,'back.log')
log = init_log(path)

log.info('This is a first message')
log.warning('This is a WARNING')
log.error('This is a ERROR')
log.debug('This is a debug')
