#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#name=input('请输入你的名字: ')
#print('hello ', name)

#age=10
#if age>5:
#    print('boy')
#else:
#    print('man')

a='abc'
b=a
a='xyz'
print(b)

PI=3.14
print(PI);

print('中文字符测试')

s = 'Python 中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

age = 20
if age>20:
    print('20')
elif age==20:
    print('222');
else:
    print('xxx')

s = input('birth：')
birth = int(s)
if birth<2000:
    print('00前')
else:
    print('00后')