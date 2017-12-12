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
