# 继承功能
class Monster():
    # 初始值
    def __init__(self, hp=100):
        self.hp = hp
    def run(self):
        print('running, the hp value=%s' %(self.hp))

class Animals(Monster):
    def __init__(self, hp=1):
        self.hp = hp

class Bpss(Monster):
    pass

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