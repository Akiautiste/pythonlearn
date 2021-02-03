# coding:utf-8

from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(now, type(now))
str_date = now.strftime('%Y-%m-%d %H:%M:%S')  # 时间对象转时间字符串
print(str_date, type(str_date))

new_obj = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')  # 时间字符串转时间对象
print(new_obj, type(new_obj))

three_days = timedelta(days=3)
print(three_days)
after_three_day = now + three_days
print(after_three_day)
