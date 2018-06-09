# 函数用法

# # 关键字参数
# print('123', end='a\n')
#
#
# def func(a, b, c):
#     print('a= %s' %a)
#     print('b= %s' % b)
#     print('c= %s' % c)
#
# func(1, 2, 3)
# # 关键字传参，可忽略顺序
# func(1, c=3, b=2)

# 可变长参数，用*特殊字符标识
def func2(a, *b):
    return 1 + len(b)

print(func2(1))
print(func2(1 , 2, 3))


# 函数作用域，global关键字声明的全局，否则不影响值的变化
name = 'hm'

def test():
    global name
    name = 'bg'
    print(name)

test()
print(name)
