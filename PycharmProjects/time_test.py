# time库

# 当前时间
import time

print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y%m%d%H%M%S'))


# 日期计算
import datetime
print()
print(datetime.datetime.now())

# 十分钟后的时间
newTime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newTime)

# 某一天+10天的时间
one_day = datetime.datetime(2008,6,18)
new_date = datetime.timedelta(days=10)
print(one_day + new_date)