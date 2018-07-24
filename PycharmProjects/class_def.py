# user1 = {'name':'hemin','age':50}
# user2 = {'name':'minbo','age':20}
#
# def print_role(rolename):
#     print('name is %s , age is %s ' %(rolename['name'], rolename['age']) )
#
# print_role(user1)
# print_role(user2)

class Player():
    def __init__(self, name ,age, hp):
        self.__name = name  # 此参数不可被外部访问
        self.age = age
        self.hp = hp
    def print_role(self):
        print('%s \'s age is %s, the job is %s' %(self.__name, self.age, self.hp))
    def updateName(self, newName):
        self.name = newName

user1 = Player('tom', 20, 'police man')
user2 = Player('linda',25,'doctor')

user1.print_role()
user2.print_role()

user1.updateName('will')
user1.print_role()

user1.name = 'Joli1bac'
user1.print_role()

class Monster():
    'for test'
    pass