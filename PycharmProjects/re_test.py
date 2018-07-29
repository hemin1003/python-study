# 正则表达式

# . 匹配任意单个字符
# ^ 匹配以字符为开头
# $ 匹配以字符为结尾
# * 匹配0次或多次
# + 匹配1次或多次
# ? 匹配0次或1次
# {m} 匹配出现指定的次数
# {m,n} 匹配出现指定的次数范围
# [] 匹配出现指定字符，比如[bcd]
# | 匹配出现指定字符
# \d 匹配数字
# \D 匹配非数字
# \s 匹配字符串
# () 分组

# ^$ 匹配空行
# .*? 不适用贪婪模式，只匹配第一个出现的内容


import re

# p = re.compile('ca.*?')
# print(p.match('ct'))
# print(p.match('cat'))
# print(p.match('caat'))
# print(p.match('caaaaaaaat'))
#
# p1 = re.compile('.{3}')
# print(p1.match('abc'))
#
# # r表示不转义输出
# print(r'\nx\n')


# 匹配日期
p3 = re.compile(r'(\d+)-(\d+)-(\d+)')
# 对应数字代表对应部分
print(p3.match('2018-05-01').group(1))
# 一次性取出所有
print(p3.match('2018-05-01').groups())
# 赋值
year , month , day = p3.match('2018-05-01').groups()
print(year)
print(month)
print(day)