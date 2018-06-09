# 上下文管理器 with用法

# 旧案例
fd = open('name.txt')
try:
    for line in fd:
        print(line)
finally:
    fd.close()


# 用with用法，新写法，不用再写finally块，with自带处理了
with open('name.txt') as f:
    for line in f:
        print(line)