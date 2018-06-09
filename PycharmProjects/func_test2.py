# 函数的迭代器和生成器

# list1 = [1, 2, 3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print((nextit))
# print(next(it)) # except

# 迭代器
# for i in range(10, 20, 2):
#     print(i)

# yield关键字，生成器，每次都记录当前位置返回
def frange(start, stop, step):
    x = start
    while x < stop:
        yield float(x)
        x += step

for i in frange(10, 20, 0.5):
    print(i)