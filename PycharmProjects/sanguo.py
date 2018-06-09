# 统计出现的名称，和兵器

# # 读取人物名称
# f = open('name2.txt')
# data = f.read()
# print(data.split('|'))
#
# # 读取兵器
# f2 = open('weapon.txt')
# i = 1
# for line in f2.readlines():
#     if i % 2 == 1:
#         print(line.strip('\n'))
#     i += 1;
#
# # 读取正文
# f3 = open('sanguo2.txt', encoding='GB18030')
# print(f3.read().replace('\n',''))

def getName(fileName):
    print(open(fileName).read())
    print('this is function')

getName('name2.txt')
getName('weapon.txt')