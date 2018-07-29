import os
print(os.path.abspath('.'))
print(os.path.abspath('..'))

print(os.path.exists('/Users'))
print(os.path.isdir('/Users'))
print(os.path.isfile('/Users'))

# 第二个参数前面不能加/
print(os.path.join('/tmp/a','b/c'))


from pathlib import Path
p = Path('.')
# 解析成路径
print(p.resolve())
print(p.is_dir())
print(p.is_file())

q = Path('/tmp/a/b/c')
# parents表示是否自动创建父目录
Path.mkdir(q, parents=True)