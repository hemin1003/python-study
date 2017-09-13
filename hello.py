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