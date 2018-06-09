# 列表推导式，字典推导式

# 案例1，所有偶数的平方

# 常规写法
a_list = []
for i in range(1,11):
    if(i % 2 == 0):
        a_list.append(i * i)

print(a_list)

# 列表推导式，优雅方式
b_list = [i*i for i in range(1,11) if(i % 2 == 0)]
print(b_list)


# 案例2，初始化字典
zodiac_name = (u'摩羯座', u'狮子座',
               u'水瓶座', u'天蝎座')

# 定义字典，初始化（不简洁优雅）
z_num = {}
for i in zodiac_name:
    z_num[i] = 0
print(z_num)

# 字典推导式，优雅方式
z_num2 = {key:0 for key in zodiac_name}
print(z_num2)
print(type(z_num2))

z_num3 = {key:0 for key in zodiac_name}
print(z_num3)