# 内置函数的用法filter(), map(), reduce(), zip()

# filter()用法
a = [1,2,3,4,5,6,7]
result = list(filter(lambda x: x>2, a))
print(result)

a = [1,2,3]
result = list(map(lambda x:x+1, a))
print(result)

b = [4,5,6]
result = list(map(lambda x,y:x+y, a, b))
print(result)

# 案例，参数成对合并
for i in zip((1,2,3),(4,5,6)):
    print(i)

# 案例
dict1 = {'name':'minbo', 'age':'100'}
print(dict1)
# key和value对调
dict2 = zip(dict1.values(), dict1.keys())
print(dict(dict2))