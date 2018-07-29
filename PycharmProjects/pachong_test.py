# 网络请求案例
from urllib import request
from urllib import parse

url = 'http://www.baidu.com';
response = request.urlopen(url, timeout=1)
print(response.read().decode('utf-8'))

# post请求
data = bytes(parse.urlencode({'word':'hello'}), encoding='utf8')
response3 = request.urlopen('http://httpbin.org/post', data=data)
print(response3.read())

# get请求
response2 = request.urlopen('http://httpbin.org/get', timeout=1)
print(response2.read())


# 超时异常处理
import urllib
import socket

try:
    response4 = request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time out')