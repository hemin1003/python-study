# 装饰器高级用法

# 装饰器用法可带参数
def new_tips(argv):
    def tips(func):
        def wrapper(a,b):
            print('start %s %s' %(argv, func.__name__))
            func(a,b)
            print('end')
        return wrapper
    return tips


# 案例，计算程序运行时间，语法糖
@new_tips('add_module')
def add(a,b):
    print(a+b)

@new_tips('sub_module')
def sub(a,b):
    print(a-b)

add(1,2)
sub(1,1)