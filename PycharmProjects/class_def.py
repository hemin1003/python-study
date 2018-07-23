# user1 = {'name':'hemin','age':50}
# user2 = {'name':'minbo','age':20}
#
# def print_role(rolename):
#     print('name is %s , age is %s ' %(rolename['name'], rolename['age']) )
#
# print_role(user1)
# print_role(user2)

class Player():
    def __init__(self, name ,age):
        self.name = name
        self.age = age
    def print_role(self):
        print('%s\'s age is %s' %(self.name, self.age))

user1 = Player('tom', 20)
user2 = Player('linda',25)

user1.print_role()
user2.print_role()
