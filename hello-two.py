#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello,world, again')
print('this is','my','second demo of python')
print(100)
print(100+200)
print('100+200')
# 注释
#name = input('please enter your name: ')
#print('hello', name)

a = 100
if a >= 1000:
    print(a)
elif a == 100:
    print(250)
else:
    print(-1)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

#s = input('birth：')
#birth = int(s)
#if birth>2000:
#    print('00后')
#else:
#    print('00前')

names = ['Michelle','Bob','Tracy']
for name in names:
    print(name)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n >0 :
    sum = sum + n
    n = n - 2
print(sum)


# 请利用循环依次对list中的每个名字打印出Hello, xxx!
# L = ['Bart', 'Lisa', 'Adam']
L = ['Bart', 'Lisa', 'Adam']
for s in L:
    print('hello', s)

n1 = 255
print('n1=', n1)
s1 = hex(n1)
print('s1=', s1)

# 定义一个函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-99))

# 定义一个空函数
def nop():
    pass

print('空函数不影响执行')

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
sum = calc(*nums)
print(sum)

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city':'beijing', 'job':'engineer'}
person('Minbo', 26, city='beijing', gender='male')
person('Minbo', 26, city=extra['city'], job=extra['job'])
person('Minbo', 26, **extra)

# 命名关键字参数
def persons(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('persons name:', name, 'age:', age, 'others:', kw)

persons('test', 100, zipcode='123456')

def person2(name, age, *, city='hunan', job):
    print(name, age, city, job)

person2('zhangsan',90,job='j')

# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数
