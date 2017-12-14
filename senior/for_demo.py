# for key
d = {'name':'hm', 'age':26}
for key in d:
    print(key)

# for values
d = {'name':'hm', 'age':26}
for value in d.values():
    print(value)

# for str
for s in 'ABC':
    print(s)

# for index
for i,value in enumerate(['A','B','C']):
    print(i, value)

for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)

print('find min and max value')

def findMinAndMax(L):
    Max = Min = L[0]
    for i in L:
        if i>=Max:
            Max = i
        elif i<=Min:
            Min = i
        L = L[1:]
    return (Min, Max)

L = [5, 1, 2, 4, 10, 6, 2, 2, 3, 9]
B = [3, 6, 7, 2, 9, 50, 10, 22, 33]
print(findMinAndMax(L))
print(findMinAndMax(B))