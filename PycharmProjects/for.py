# for循环用法

str = 'abcde'
for s in str:
    print(s)

for i in range(5):
    print(i)

for i in range(0,5):
    print(i)
    print(str[i])
    print('%s 的下标的值为 %s' %(i, str[i]))

for i in range(0,10,2):
    print(i)


zodiac_name = (u'摩羯座', u'狮子座',
               u'水瓶座', u'天蝎座')
zodiac_days = ((1,20), (2, 19), (3,21), (4,21))

int_month = int(input('请输入月份：'))
int_day = int(input('请输入日期：'))

for zd_num in range(len(zodiac_days)):
    if zodiac_days[zd_num] >= (int_month, int_day):
        print(zodiac_name[zd_num])
        break;
    elif int_month >= 4 and int_day > 21:
        print(zodiac_name[0])
        break;
    elif int_month > 4:
        print(zodiac_name[0])
        break;