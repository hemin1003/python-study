# 字典多层嵌套

# 首先我们可以定义一个非嵌套的字典
dict1 = {'tom': 'a', 'jerry': 'b'}

# 为非嵌套的字典增加一个新的键/值对，赋值的类型是字符串
dict1['mary1'] = 'c'

# 输出新的字典的内容
print('没有嵌套的字典 %s' % dict1)

# 如果mary2本身就是一个字典可以直接像字符串一样增加到dict1中
dict1['mary2'] = {'name': 'mary mary', 'age': 18}

# 输出新的字典的内容
print('有嵌套的字典 %s' % dict1)

# 输出外层字典的内容
print(dict1['mary2'])

# 输出内层字典的内容
print(dict1['mary2']['age'])