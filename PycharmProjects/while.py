# while用法
import time

# a = 5
# while True:
#     a = a + 1
#
#     if a == 10:
#         continue;
#         # break;
#
#     print(a)
#     # 引入休眠组件，单位为秒
#     time.sleep(1)


zodiac_name = (u'摩羯座', u'狮子座',
               u'水瓶座', u'天蝎座')
zodiac_days = ((1,20), (2, 19), (3,21), (4,21))

int_month = int(input('请输入月份：'))
int_day = int(input('请输入日期：'))

n = 0
while zodiac_days[n] < (int_month, int_day):
    if int_month ==4 and int_day > 21:
        break;
    elif int_month>4:
        break;
    n += 1

print(zodiac_name[n])

