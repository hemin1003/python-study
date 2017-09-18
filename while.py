#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#names = ['wangming', 'minbo', 'test']
#for name in names:
#    print(name)

#sum = 0
#for x in [1,2,3,4,5]:
#    sum = sum + x
#print(sum)

#sum = 0
#for x in range(101):
#    sum = sum + x
#print(sum)

sum = 0
n = 99
while n>0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    if name == 'Lisa':
        continue
    print('hello ' + name)