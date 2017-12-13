#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

print('欢迎玩此游戏')
secret = random.randint(1,10)
temp = input('请猜下我心中的数字: ')
guess = int(temp)
while guess !=secret :
    temp = input('猜错啦，继续猜我心中的数字: ')
    guess = int(temp)
    if(guess == secret):
        print('猜中了')
        print('你真牛')
    else:
        if guess > secret:
            print('大了')
        else:
            print('小了')
print('游戏结束')