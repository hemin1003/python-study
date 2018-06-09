# 元组用法，元素不可更改

print((4) > (5))
print((4+2) > (5+0))
print((5,1) > (5,0))

str = ('abc','123')
# 不能更改
# str[0] = 'xyz'
print(str[0])

# u表示unicode，避免乱码
# 假设定义
zodiac_name = (u'摩羯座', u'狮子座',
               u'水瓶座', u'天蝎座')

zodiac_days = ((1,20), (2, 19), (3,21), (4,21))

(month, day) = (2, 15)
# 过滤器用法
zodiac_day = filter(lambda x: x<=(month, day), zodiac_days)

print(zodiac_day)

zodiac_len = len(list(zodiac_day)) % 12
print(zodiac_name[zodiac_len])