# 序列有字符串、列表、元组

# 字符串
str = 'abcde'
print(str[0])
print(str[-1])
print(str[1:2])

name = "my name's minbo"
print(name)

# 常用的操作有：
# 成员关系操作符：in, not in
# 连接操作符：+
# 重复操作符：*x
# 切片操作符：[x:x]，含前者下标，不含后者下标

str = 'abcde'
a = 'a'

print(a in str)
print(a not in str)

print(str + str)
print(str + '123')

print(str*3)

print(str[1:2])