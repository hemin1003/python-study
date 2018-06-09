# 条件判断

a = 2

if a < 1:
    print('小于')

elif a >2:
    print('大于')

else:
    print('不符合')
    print('a=2')

b = 100
if b == 100:
    print(b)

# 用户输入
str = 'abcde';
# 转换成数字，否则不能计算。输入都是字符串
year = int(input('请输入年份：'))
print(year)

print(str[year % 5])

if str[year % 5] == 'd':
    print('this is d')