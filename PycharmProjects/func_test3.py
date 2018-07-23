# 闭包函数用法

# 案例
# def sum(a):
#     def add(b):
#         return a+b
#     return add
#
# num = sum(1)
# print(num(2))


# 案例2，计数器
# def counter(First=0):
#     cnt = [First]
#     def add_one():
#         cnt[0] += 1
#         return cnt[0]
#     return add_one
#
# num5 = counter(5)
# print(num5())
# print(num5())
# print(num5())
#
# num10 = counter(10)
# print(num10())
# print(num10())
#
# num0 = counter()
# print(num0())
# print(num0())

# 案例3，计算a*x + b = y
# def line(a, b):
#     def arg_y(x):
#         return a*x + b
#     return arg_y

# 或者，lambda表达式，匿名函数
def line(a, b):
    return lambda x: a * x + b


a_line = line(1, 2)
print(a_line(2))
print(a_line(10))
