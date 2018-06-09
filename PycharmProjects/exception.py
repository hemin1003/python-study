# 异常处理

# NameError
# i = j

# SyntaxError
# print(1))

# IndexError
# a = ['abc']
# print(a[3])

# KeyError
# dict1 = {'a':1, 'b':2}
# print(dict1['c'])

# ValueError
# try:
#     year = int(input('please input: '))
# except ValueError:
#     print('请输入数字')

# TypeError
# print(year / 'a')

# try:
#     a = 123
#     a.append()
# except (AttributeError,ValueError):
#     print('无此方法，请确认')

# try:
#     print(1/'a')
# except (TypeError,ZeroDivisionError) as e:
#     print('异常了，请处理 %s' %e)

# 捕获所有异常
# try:
#     print(1/'a')
# except Exception as e:
#     print('异常了，请处理 %s' %e)


# 自定义异常，用关键字：raise
# try:
#     raise NameError('helloError')
# except Exception:
#     print('my custom error')

# finally
try:
    file1 = open('name1.txt')
except Exception as e:
    print(e)
finally:
    file1.close()
    print('close file')