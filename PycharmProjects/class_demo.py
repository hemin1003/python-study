# 继承功能
class Monster():
    # 初始值
    def __init__(self, hp=100):
        self.hp = hp
    def run(self):
        print('running, the hp value=%s' %(self.hp))
    def whoami(self):
        print('i am Monster')

class Animals(Monster):
    def __init__(self, hp=1):
        self.hp = hp

class Boss(Monster):
    def whoami(self):
        print('i am boss')

class Test():
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print('my name is %s' %(self.name))

a1 = Monster()
print(a1.hp)
print(a1.run())

a2 = Animals(10)
print(a2.hp)
print(a2.run())

a3 = Animals(210)
print(a3.hp)
print(a3.run())

test1 = Test('minbo')
test1.print_name()

boss1 = Boss()
boss1.whoami()

# 判断父类/子类
print('a1的类型 %s' %type(a1))
print('a2的类型 %s' %type(a2))
print('a3的类型 %s' %type(a3))

print(isinstance(test1, Monster))
print(isinstance(a1, Monster))
print(isinstance(a2, Monster))