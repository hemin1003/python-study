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



