# 装饰器用法
import time

def timer(func):
    def wrapper():
        start_time = time.time();
        func()
        stop_time = time.time()
        print('程序运行了 %s 秒' %(stop_time - start_time))
    return wrapper


# 案例，计算程序运行时间，语法糖
@timer
def i_can_sleep():
    print('正在执行业务逻辑处理...')
    time.sleep(3)


# start_time = time.time();

i_can_sleep()

# stop_time = time.time()
# print('程序运行了 %s 秒' %(stop_time - start_time))