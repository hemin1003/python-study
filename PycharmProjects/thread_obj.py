import threading
from threading import current_thread

class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


my1 = MyThread()
my1.start()
my1.join()
print(current_thread().getName(), 'end')