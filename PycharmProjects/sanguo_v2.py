import re

def find_item(name):
    with open('sanguo2.txt', encoding='GB18030') as f:
        data = f.read().replace('\n','')
        name_num = re.findall(name, data)
        # print('名称 %s 出现了 %s 次' %(name, len(name_num)))
    return len(name_num)





# 读取人物信息
name_dict = {}
with open('name2.txt') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            # print(n)
            name_num = find_item(n)
            name_dict[n] = name_num

print(name_dict)

name_sorted = sorted(name_dict.items(), key= lambda item: item[1], reverse=True)
print(name_sorted)