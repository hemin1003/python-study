# with用法

class TestWith():
    def __enter__(self):
        print('run')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('exit')
        else:
            print('exception here %s' %exc_tb)


# 异常不用特例捕获，with语句已自定带有处理，代码看起来更加简洁
with TestWith():
    print('Test is running')
    # 手动抛出异常
    raise NameError('testNameError')