# 文件基础操作
# 内建函数open(), read(), readline(), seek(), write(), close()

# file1 = open('name.txt', mode='w')
# file1.write('minbo')
# file1.write('minbo')
# file1.write('minbo')
# file1.close()
#
# file2 = open('name.txt')
# content = file2.read()
# print(content)
# file2.close()

# mode=a表示文件内容追加，默认是r=只读，w=可写
# file3 = open('name.txt', mode='a')
# file3.write('hemin')
# file3.close()

# file4 = open('name.txt')
# content = file4.readline()
# print(content)
# file4.close()

# 读取所有内容
# file5 = open('name.txt')
# for line in file5.readlines():
#     print(line)

file6 = open('name.txt')
print('当前文件指针的位置：%s' %file6.tell())

print('当前读取到了一个字符，内容是 %s' %file6.read(1))
print('当前文件指针的位置：%s' %file6.tell())

# 第一个参数代表偏移的位置，第二个参数：0=从文件开头开始偏移，1=从当前位置开始偏移，2=从文件结尾
file6.seek(3,0)
print('进行了seek()操作')
print('当前文件指针的位置：%s' %file6.tell())

print('当前读取到了一个字符，内容是 %s' %file6.read(1))
print('当前文件指针的位置：%s' %file6.tell())
file6.close()