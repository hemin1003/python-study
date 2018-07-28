import threading
import time
from threading import current_thread

# 不带多线程的实例

def myThread(arg1, arg2):
    print(current_thread().getName(), 'start')
    time.sleep(1)
    print('%s %s' %(arg1, arg2))
    print(current_thread().getName(), 'stop')

for i in range(1,6,1):
    # 顺序执行结果
    # t1 = myThread(i, i+1)
    # 多线程执行结果
    t2 = threading.Thread(target=myThread, args=(i, i + 1))
    t2.start()
    # t2.join()

print(current_thread().getName(), 'end')
