# 字典用法，key，value

dict1 = {}
print(type(dict1))

dict2 = {'name':'minbo', 'age':100}
dict2['weight'] = 100
print(dict2)

dict3 = {'x':'x', 'y':1}
dict2['z'] = 100
print(dict2)

# 用字典记录星座的数量
zodiac_name = (u'摩羯座', u'狮子座',
               u'水瓶座', u'天蝎座')
zodiac_days = ((1,20), (2, 19), (3,21), (4,21))

# 定义字典，初始化
z_num = {}
for i in zodiac_name:
    z_num[i] = 0

while True:
    int_month = int(input('请输入月份：'))
    int_day = int(input('请输入日期：'))

    n = 0
    while zodiac_days[n] < (int_month, int_day):
        if int_month == 4 and int_day > 21:
            break;
        elif int_month > 4:
            break;
        n += 1

    print(zodiac_name[n])
    z_num[zodiac_name[n]] += 1

    # 输出统计
    for each_key in z_num.keys():
        print('星座 %s 有 %d 个' %(each_key, z_num[each_key]))